from create_excel import create_excel, settings_merge, create_header
from functions import separate_first_raw, separate_and_check_all_fields

input_file = "text.txt"
output_file = "hello.xlsx"

my_file = open(input_file, "r", encoding="utf-8")
workbook = create_excel(output_file)
worksheet = workbook.add_worksheet()
merge_format = settings_merge(workbook)

raw = 1
column = 0
test = 0
raw_domain = 1
raw_site = 1
sum_category = 1
raw_category = 1

create_header(worksheet)

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

        domain = separate_first_raw(previous_line, current_line)
        site = separate_and_check_all_fields(previous_line, current_line, 1)
        category = separate_and_check_all_fields(previous_line, current_line, 2)

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
else:
    print("Please input file")


workbook.close()
