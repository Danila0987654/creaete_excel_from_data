def separate_first_raw(previous_line, current_line):
    something = []

    previous_list = previous_line.split(",")
    current_list = current_line.split(",")
    if previous_list[0] != current_list[0]:
        something.append(current_list)
    else:
        something.append(0)

    return something


def separate_and_check_all_fields(previous_line, current_line, field):
    something = []

    previous_list = previous_line.split(",")
    current_list = current_line.split(",")
    if previous_list[field] != current_list[field] or \
            previous_list[1] != current_list[1] or previous_list[0] != current_list[0]:
        something.append(current_list)
    else:
        something.append(0)

    return something