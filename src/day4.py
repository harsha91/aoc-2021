from pprint import pprint
from data import day4

draws = day4.draws
matrixes = day4.matrixes

# draws = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

# matrixes = """
# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7
#  """

def check_finish(mat):
    finish = False
    # pprint(mat)
    for i in range(0,5):
        row_sum = 0
        col_sum = 0 
        for j in range(0,5):
            row_sum += list(mat[i][j].values())[0]
            col_sum += list(mat[j][i].values())[0]
        if row_sum==5 or col_sum==5:
            finish = True
            break
    return finish


def calc_sum(mat):
    nums_set = set()
    for row in mat:
        for tups in row:
            if 0 == list(tups.values())[0]:
                nums_set.add(list(tups.keys())[0])
    return sum(nums_set)


def first_puzzle():
    finish_num = -1 
    for n in draws:
        for mat in mats:
            for row in mat:
                for tups in row:
                    if n == list(tups.keys())[0]:
                        tups[n] = 1
            
            if check_finish(mat):
                print("Finish at " + str(n))
                finish_num = n
                print(n * calc_sum(mat))
                break
        if finish_num != -1:
            break

if __name__ == "__main__":
    i = 0 
    mats = []
    columns = []
    
    for matrix in matrixes.split("\n"):
       rows = []
       
       if not matrix:
           continue
       
       for row in matrix.split(" "):
            if not row:
                continue
            rows.append({int(row): 0})
       
       if rows:    
            columns.append(rows)
            i += 1
       
       if i == 5:
            if columns:
                mats.append(columns)
            columns = []
            i = 0
    
    first_puzzle()
    
    tats = []
    finish_num = -1
    for n in draws:
        for mat in mats:
            for row in mat:
                for tups in row:
                    if n == list(tups.keys())[0]:
                        tups[n] = 1
            if check_finish(mat) and mat not in tats:
                tats.append(mat)

            if len(tats) == len(mats):
                finish_num = n
                print("Finish at " + str(n))
                print(n * calc_sum(mat))
                break
            

        if finish_num != -1:
            break
