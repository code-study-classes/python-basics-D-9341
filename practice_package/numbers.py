calculate_distance = lambda x, y: abs(x - y)

calculate_segments = lambda a, b: a // b

calculate_digit_sum = lambda numby: sum(int(i) for i in str(numby))

calculate_rect_area = lambda x1, y1, x2, y2: (x2 - x1) * (y2 - y1)

round_to_multiple = lambda numby, multiple: round(numby / multiple) * multiple
