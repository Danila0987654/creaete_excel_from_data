import xlsxwriter


def create_excel(filename):
    workbook = xlsxwriter.Workbook(filename)

    return workbook


def create_header(worksheet):
    worksheet.write(0, 0, "id")
    worksheet.write(0, 1, "domain")
    worksheet.write(0, 2, "firewall")
    worksheet.write(0, 3, "category")


def settings_merge(workbook):
    merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter'})

    return merge_format