from pprint import pprint
from data import day6

input = day6.input

input1 = [3,4,3,1,2]

def calc_fishes(fishes, days):
    while days > 0:
        add_fish = 0
        tmp_fishes = []
        for fish_day in fishes:
            if fish_day == 0:
                add_fish += 1
                tmp_fishes.append(6)
            else:
                tmp_fishes.append(fish_day-1)
        fishes = tmp_fishes
        while add_fish > 0:
            fishes.append(8)
            add_fish -= 1
        days -= 1
    return fishes
    
if __name__ == '__main__':
    days = 80
    # print(f'Total number of fish: {len(calc_fishes(input, days))}')
    fishes = input
    days = [0] * 9
    # Update the current numbers
    for fish in fishes:
        days[fish] += 1
    print(days)
    for i in range(256):
        # To make it cyclic: 0, 1, 2, 3, 4, 5, 6, 7, 8  
        today = i % len(days)
        # Add new babies
        days[(today + 7) % len(days)] += days[today]

    print(days)
    print(f'Total lanternfish after 256 days: {sum(days)}')