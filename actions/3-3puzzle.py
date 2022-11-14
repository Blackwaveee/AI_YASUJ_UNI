import random
class Puzzle:
    def __int__(self,map):
        self.map = map

    def __init__(self,length = 3,makeRandom = True):
        if makeRandom:
            arr = []
            maxNum = length ** 2 - 1
            loopLen = maxNum

            while loopLen > -1:
                num = random.randint(0,maxNum)
                print(num)
                if num in arr:
                    continue
                arr.append(num)
                loopLen-=1
            self.map = [[arr[i*length + j] for j in range(length)] for i in range(length)]
        else:
            self.map = [[i*length+j+1 for j in range(length)] for i in range(length)]
            self.map[length-1][length-1] = 0

print(Puzzle(3).map)