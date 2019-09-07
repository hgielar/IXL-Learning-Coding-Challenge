
def countholes(num):
    holes_num = 0
    for char in str(num):
        if char in map(str, [0 ,4 ,6 ,9]):
            holes_num += 1

        elif char == '8':
            holes_num += 2

    return holes_num
