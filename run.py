import xlsxwriter


def do_stuff_with_two_lines(previous_line, current_line, field, double_check):
    something = []

    previous_list = previous_line.split(",")
    current_list = current_line.split(",")
    if double_check == "false":
        if previous_list[field] != current_list[field]:
            something.append(current_list)
        else:
            something.append(0)
    else:
        if previous_list[field] != current_list[field] or \
                previous_list[1] != current_list[1] or previous_list[0] != current_list[0]:
            something.append(current_list)
        else:
            something.append(0)

    return something


my_file = open('text.txt', 'r', encoding="utf-8")
workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()
raw = 1
column = 0
test = 0
raw_domain = 1
raw_site = 1
sum_category = 0
raw_category = 1

worksheet.write(0, 0, "domain")
worksheet.write(0, 1, "site")
worksheet.write(0, 2, "firewall")
worksheet.write(0, 3, "category")

merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter'})

if my_file:
    current_line = my_file.readline()

first_line_value = current_line.split(",")
first_line_domain = first_line_value[0]
first_line_url = first_line_value[1]
first_line_value = first_line_value[2]

for line in my_file:
    raw += 1
    previous_line = current_line
    current_line = line

    domain = do_stuff_with_two_lines(previous_line, current_line, 0, "false")
    site = do_stuff_with_two_lines(previous_line, current_line, 1, "true")
    category = do_stuff_with_two_lines(previous_line, current_line, 2, "true")

    for i in domain:
        if i != 0:
            if raw_domain == 1:
                worksheet.merge_range(raw_domain, 0, raw, 0, first_line_domain, merge_format)
            else:
                worksheet.merge_range(raw_domain, 0, raw, 0, i[0], merge_format)
            raw_domain = raw + 1
    for i in site:
        if i != 0:
            if raw_site == 1:
                worksheet.merge_range(raw_site, 1, raw, 1, first_line_url, merge_format)
            else:
                worksheet.merge_range(raw_site, 1, raw, 1, i[1], merge_format)
            raw_site = raw + 1
    for i in category:
        if i != 0:
            if raw_category == 1:
                worksheet.merge_range(raw_category, 3, raw, 3, first_line_url, merge_format)
                worksheet.merge_range(raw_category, 2, raw, 2, sum_category, merge_format)
            else:
                worksheet.merge_range(raw_category, 3, raw, 3, i[2], merge_format)
                worksheet.merge_range(raw_category, 2, raw, 2, sum_category, merge_format)
            raw_category = raw + 1
            sum_category = 1
        else:
            sum_category += 1

    raw += 1


workbook.close()
