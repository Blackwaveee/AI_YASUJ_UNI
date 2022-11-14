import sys
sys.path.append("..")
import time

class Node:

    def __copy__(self):
        return Node(self.L.copy(),self.R.copy(),self.boat).pre(self)

    def __init__(self,L,R,boat = False):
        self.L = L
        self.R = R
        self.boat = boat
        self.prev = None

        #True : right
        #False : left

    def pre(self,pre = None):
        if pre is None:
            return self.prev
        self.prev = pre
        return self

    def equal(self,node):
        return node.L == self.L and node.R == self.R and node.boat == self.boat

    def reverseBoat(self):
        self.boat = not self.boat
        return self

    def addRight(self,missionaries,cannibals):
        self.R[0] += missionaries
        self.R[1] += cannibals
        self.L[0] -= missionaries
        self.L[1] -= cannibals
        return self

    def addLeft(self,missionaries,cannibals):
        self.L[0] += missionaries
        self.L[1] += cannibals
        self.R[0] -= missionaries
        self.R[1] -= cannibals
        return self

    def add(self,missionaries,cannibals):
        if self.boat:
            return self.addLeft(missionaries,cannibals)
        return self.addRight(missionaries,cannibals)

    def missionaries(self,R = True):
        return self.R[0] if R else self.L[0]

    def cannibals(self,R = True):
        return self.R[1] if R else self.L[1]

    def isRightFull(self):
        return self.R == [3,3]

    def canAdd(self,missionaries,cannibal):
        if self.boat:
            return (self.R[0] - missionaries == 0 or self.R[0] - missionaries >= self.R[1] - cannibal) and (self.L[0] + missionaries == 0 or self.L[0] + missionaries >= self.L[1] + cannibal)
        return (self.L[0] - missionaries == 0 or self.L[0] - missionaries >= self.L[1] - cannibal) and (self.R[0] + missionaries == 0 or self.R[0] + missionaries >= self.R[1] + cannibal)

    def moves(self):
        moves = []

        missionaries,cannibals = self.missionaries(self.boat),self.cannibals(self.boat)

        if missionaries > 1 and self.canAdd(2,0):
            moves.append(self.__copy__().add(2,0).reverseBoat())

        if cannibals > 1 and self.canAdd(0,2):
            moves.append(self.__copy__().add(0,2).reverseBoat())

        if missionaries and self.canAdd(1,0):
            moves.append(self.__copy__().add(1,0).reverseBoat())

        if cannibals and self.canAdd(0,1):
            moves.append(self.__copy__().add(0,1).reverseBoat())

        if missionaries and cannibals and self.canAdd(1,1):
            moves.append(self.__copy__().add(1,1).reverseBoat())

        return moves

    def print(self):
        print('right' if self.boat else 'left')
        print('L:',str(self.L[0])+'M ,',str(self.L[1])+'C')
        print('R:',str(self.R[0])+'M ,',str(self.R[1])+'C')
        print('--')

    def traceBack(self):
        node = self.__copy__()
        if node is None:
            return

        while True:
            node.print()
            node=node.pre()
            if node is None:
                break

        return self

class Nodes:
    def __init__(self):
        self.nodes = []

    def exists(self,node):
        for _node in self.nodes:
            if _node.equal(node):
                return True
        return False

    def add(self,node,check = True):
        if check and self.exists(node):
            return False
        self.nodes.append(node)
        return True

    def addNodes(self,nodes,check = True):
        added = []
        for node in nodes:
            if self.add(node,check):
                added.append(node)

        return added


def solve(node,nodes):
    moves = nodes.addNodes(node.moves())

    for move in moves:
        move.print()
        time.sleep(1)
        if move.isRightFull():
            return move
        checkSolve = solve(move,nodes)
        if checkSolve:
            return checkSolve

    return False

def run(args):
    solved = solve(Node([3,3],[0,0]),Nodes())
    print('solved')
    print('--------------------------------------')
    print('trace back(route) : ')
    solved.traceBack()
    return

