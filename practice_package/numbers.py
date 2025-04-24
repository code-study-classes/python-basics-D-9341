def calculate_distance(x, y):
    return abs(x - y)


def calculate_segments(a, b):
    return a // b


def calculate_digit_sum(numby):
    return sum(int(i) for i in str(abs(numby)))


def calculate_rect_area(x1, y1, x2, y2):
    return (x2 - x1) * (y2 - y1)


def round_to_multiple(numby, multiple):
    return round(numby / multiple) * multiple
