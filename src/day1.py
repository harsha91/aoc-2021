from data import day1

input = day1.input

def first_puzzle(list_input):
    counter = 0
    previous = list_input[0]
    for i in list_input[1:]:
        if  i > previous:
            counter += 1
        previous = i
    print(counter)

if __name__ == '__main__':
    first_puzzle(input)
    counter = 0 
    sliding_list = []
    tmp = 0
    while counter+3 <= len(input):
       
        for j in input[counter:counter+3]:
            tmp = tmp + j
        
        sliding_list.append(tmp)
        tmp = 0
        counter += 1
            
    first_puzzle(sliding_list)


