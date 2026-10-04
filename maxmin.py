list = list(map(int, input("Enter numbers separated by comma: ").split(",")))

ordered_list = sorted(list)
max_min = [ordered_list[0], ordered_list[-1]]

print(max_min)
