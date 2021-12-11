from data import day3

input = day3.input

def first_puzzle():
    i = 0
    gamma = "" 
    epsilon = ""
    while i < len(input.split("\n")[1]):
        one_count = 0
        zero_count = 0
        for line in input.split("\n"):
            if not line:
                continue
            if line[i] == "1":
                one_count += 1
            else:
                zero_count += 1
        if one_count > zero_count:
            gamma += "1"  
            epsilon += "0"  
        else:
            gamma += "0"  
            epsilon += "1"  
        i += 1
    print(int(gamma, 2) * int(epsilon, 2))


def second_puzzle(flip):
    i = 0
    if flip:
        val_1 = "1"
        val_0 = "0"
    else:
        val_1 = "0"
        val_0 = "1"
    
    input_lines = []
    
    for l in input.split("\n"):
        if l:
            input_lines.append(l)
    tmp_list = input_lines
    
    while i < len(input_lines[0]) and len(tmp_list) > 1:
        low_list = [] 

        one_count = 0
        zero_count = 0
        for line in tmp_list:
            if line[i] == "1":
                one_count += 1
            else:
                zero_count += 1
        
        if one_count == zero_count:
            for line in tmp_list:
               if (line[i] == val_1):
                    low_list.append(line) 
       
        elif one_count > zero_count:
            
           for line in tmp_list:
               if (line[i] == val_1):
                    low_list.append(line)
        
        else:
            for line in tmp_list:
                if (line[i] == val_0):
                    low_list.append(line)

        tmp_list = low_list
        i += 1
    return tmp_list[0]

if __name__ == "__main__":
    # first_puzzle()
    o2 = second_puzzle(True)
    co2 = second_puzzle(False)
    print(int(o2,2) * int(co2,2))