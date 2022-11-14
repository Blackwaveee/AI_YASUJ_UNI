import sys
sys.path.append("..")
import helper

class Chess:
    def __init__(self,length):
        self.clear(length)

    def clear(self,length):
        self.mat = [[0 for y in range(length)] for x in range(length)]
        return self

    def _find(self,mat):
        pass

    def find(self):


    @staticmethod
    def check(mat):
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

            sum1, sum2 = 0, 0
            for j in range(length):
                sum1 += mat[i][j]
                if sum1 == 2:
                    return False

                sum2 += mat[j][i]
                if sum2 == 2:
                    return False

        return True

    @staticmethod
    def instance(length):
        return Chess(length)

def run(args):
    length = args['length'] if 'length' in args and args['length'] else 8
    return Chess.instance(length).loop()

