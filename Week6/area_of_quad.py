var_1 = 10

def cal_area_rectangle(length_x, length_y):
    return length_x * length_y


for count in range(0, 10):
    result = cal_area_rectangle(10, count)
    print(result)


print(cal_area_rectangle(10, 78))
