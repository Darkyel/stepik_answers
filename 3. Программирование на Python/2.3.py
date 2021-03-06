/step/3

def print_multiplication_table(vertical_interval, horizontal_interval):
    print('\t', end='')
    for i in range(horizontal_interval[0], horizontal_interval[1] + 1):
        print(i, end='\t')
    print()
    for i in range(vertical_interval[0], vertical_interval[1] + 1):
        print(i, end='\t')
        for j in range(horizontal_interval[0], horizontal_interval[1] + 1):
            print(i * j, end='\t')
        print()
intervals = (int(input()), int(input())), (int(input()), int(input()))
print_multiplication_table(intervals[0], intervals[1])

/step/7

def avg_by_dividable(data, divider):
    filtered_data = [x for x in data if x % divider == 0]
    return sum(filtered_data) / len(filtered_data)
numbers = range(int(input()), int(input()) + 1)
print(avg_by_dividable(numbers, 3))
