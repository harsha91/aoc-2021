from data import day7

input = day7.input

input1 = [16,1,2,0,4,2,7,1,2,14]

# declare if main
if __name__ == "__main__":
    fuel = []
    for i in range(min(input), max(input)+1):
        tmp_fuel = 0
        for j in input:
            tmp_fuel += abs(i - j)
            if fuel and tmp_fuel > min(fuel):
                break
        fuel.append(tmp_fuel)

    print("First", min(fuel))

    fuel = []
    for i in range(min(input), max(input)+1):
        tmp_fuel = 0
        for j in input:
            tmp_fuel += int((abs(i - j)* (abs(i - j)+1))/2)
            if fuel and tmp_fuel > min(fuel):
                break
        fuel.append(tmp_fuel)
    
    print("Second", min(fuel))