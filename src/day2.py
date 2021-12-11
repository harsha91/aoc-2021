from data import day2

input = day2.input

def first_puzzle(inp):
    horizontal = 0 
    depth = 0

    for line in inp.splitlines():
        if line:
            cmd, arg = line.split()
            if cmd == 'forward':
                horizontal += int(arg)
            if cmd == 'up':
                depth += int(arg)
            if cmd == 'down':
                depth -= int(arg)
    
    print(abs(horizontal * depth))


if __name__ == '__main__':
    first_puzzle(input)
    
    horizontal = 0 
    depth = 0
    aim = 0

    for line in input.splitlines():
        if line:
            cmd, arg = line.split()
            if cmd == 'forward':
                horizontal = abs(horizontal + int(arg))
                depth = abs(depth + (aim * int(arg)))
            if cmd == 'up':
                aim = abs(aim - int(arg))
            if cmd == 'down':
                aim = abs(aim + int(arg))
    
    print(abs(horizontal * depth))