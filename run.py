import xlsxwriter


def do_stuff_with_two_lines(previous_line, current_line):
    something = []

    previous_list = previous_line.split(",")
    current_list = current_line.split(",")
    if previous_list[0] != current_list[0]:
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
raw_prev = 1

worksheet.write(0, 0, "domain")
worksheet.write(0, 1, "site")
worksheet.write(0, 2, "firewall")
worksheet.write(0, 3, "category")

merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': 'yellow'})

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

    get = do_stuff_with_two_lines(previous_line, current_line)

    for i in get:
        if i != 0:
            print(raw_prev)
            print(raw)
            print(i[0])
            if raw_prev == 1:
                worksheet.merge_range(raw_prev, 0, raw, 0, first_line_domain, merge_format)
            else:
                worksheet.merge_range(raw_prev, 0, raw, 0, i[0], merge_format)
            raw_prev = raw + 1

    raw += 1


workbook.close()
