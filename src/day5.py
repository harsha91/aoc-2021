import collections
from data import day5

input = day5.input

input1 = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

if __name__ == "__main__":
    rows = [row.split(" -> ") for row in input.split("\n") if row]
    nums = []
    nums1 = []
    cnt = 0
    for row in rows:
        x, y = (int(i) for i in row[0].split(","))
        x2, y2 = (int(i) for i in row[1].split(","))
        if y == y2:
            for i in range(0, abs(x-x2)+1):
                if(x < x2):
                    nums.append((x+i, y))
                    nums1.append((x+i, y))
                else:
                    nums.append((x2+i, y))
                    nums1.append((x2+i, y))
        elif x == x2:
            for i in range(0, abs(y-y2)+1):
                if(y < y2):
                    nums.append((x, y+i))
                    nums1.append((x, y+i))
                else:
                    nums.append((x, y2+i))
                    nums1.append((x, y2+i))
        else:
            diff = 0
            if abs(x-x2) > abs(y-y2):
                diff = abs(x-x2) 
            else:
                diff = abs(y-y2)
            for i in range(0, diff+1):
                tmpX , tmpY = 0, 0
                if(x < x2):
                    tmpX = x+i
                if(x > x2):
                    tmpX = x-i
                if(y < y2):
                    tmpY = y+i
                if(y > y2):
                    tmpY = y-i
                nums1.append((tmpX, tmpY))

    print("first", len([item for item, count in collections.Counter(nums).items() if count > 1]))
    print("second", len([item for item, count in collections.Counter(nums1).items() if count > 1]))

