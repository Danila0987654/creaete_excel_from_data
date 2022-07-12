import xlsxwriter


def do_stuff_with_two_lines(previous_line, current_line, field):
    something = []

    previous_list = previous_line.split(",")
    current_list = current_line.split(",")
    if previous_list[field] != current_list[field]:
        something.append(current_list)
    else:
        something.append(0)

    return something


my_file = open('text.txt', 'r')
workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()
raw = 1
column = 0
test = 0
raw_domain = 1
raw_site = 1

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

    domain = do_stuff_with_two_lines(previous_line, current_line, 0)
    site = do_stuff_with_two_lines(previous_line, current_line, 1)
    print(test)

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

    raw += 1


workbook.close()
