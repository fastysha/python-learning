GRADE_DICT = {
    range(90, 101): "A",
    range(80, 90): "B",
    range(75, 80): "C",
    range(65, 75): "D",
    range(60, 65): "E",
    range(0, 60): "F"
}

def get_grade(total: int, actual: int) -> str:
    percentage = (actual * 100) // total
    return get_grade_by_percentage(percentage)


def get_grade_by_percentage(percentage: int) -> str:
    filtered_key_list = [key_range for key_range in list(GRADE_DICT.keys()) if percentage in key_range]
    if len(filtered_key_list) == 0:
        raise RuntimeError('Not able to get grade by percentage: ' + percentage)
    range_key = filtered_key_list[0]
    return GRADE_DICT[range_key]

