import sys
sys.path.append("..")
import helper

class Chess:
    def __init__(self,length):
        self.clear(length)

    def clear(self,length):
        self.mat = [[0 for y in range(length)] for x in range(length)]
        return self

    def check(self):
        mat = self.mat
        sum1 = 0
        sum2 = 0
        length = len(mat)

        for i in range(length):
            sum1 += mat[i][i]
            if sum1 == 2:
                return False

            sum2 += mat[i][length - i - 1]
            if sum2 == 2:
                return False

            sum1,sum2 = 0,0
            for j in range(length):
                sum1 += mat[i][j]
                if sum1 == 2:
                    return False

                sum2 += mat[j][i]
                if sum2 == 2:
                    return False

        return True

    def put(self,x,y):
        length = len(self.mat)

        if x < 0 or x >= length or y < 0 or y >= length:
            return 'Invalid point'

        self.mat[x][y] = 1

        if not self.check() :
            self.mat[x][y] = 0
            return 'Point cross'

        return True

    def showTable(self):
        length = len(self.mat)
        print('  ',end='')
        for i in range(length):
            print(i+1,end=' ')
        print()
        for i in range(length):
            print(i+1,end=' ')
            for j in range(length):
                print(self.mat[i][j],end = ' ')
            print()
        return self

    def loop(self):
        length = len(self.mat)
        i = 0
        while i < length:

            helper.clear()
            self.showTable()
            print()
            x = helper.readInt(prefix='x',_range=(1,length)) - 1
            y = helper.readInt(prefix='y',_range=(1,length)) - 1

            result = self.put(x, y)

            input(('Next move' if result is True else 'try again') + ', press enter to continue')
            i += 1 if result is True else 0

        helper.clear()
        self.showTable()
        print('Done')

        return None

    @staticmethod
    def instance(length):
        return Chess(length)

def run(args):
    length = args['length'] if 'length' in args and args['length'] else 8
    return Chess.instance(length).loop()

