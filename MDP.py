import random

class MDP():

    def __init__( self, grid ):
        print("init")
        self.G = grid
        self.A = ['^', 'v', '>', '<']
        self.gama = .9
        self.U = []
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[i])):
                row.append(0)
            self.U.append(row)
        self.policy = []

    def up(self, i, j):
        if i-1 == -1:
            x = self.U[i][j]
            return (x)
        try:
            x = self.U[i-1][j]
            return (x)
        except:
            u = self.U[i][j]
            return()
    def left(self, i, j):
        if j-1 == -1:
            x = self.U[i][j]
            return (x)
        try:
            x = self.U[i][j-1]
            return (x)
        except:
            u = self.U[i][j]
            return(u)

    def down(self, i, j):
        try:
            x = self.U[i+1][j]
            return (x)
        except:
            u = self.U[i][j]
            return(u)

    def right(self, i, j):
        try:
            x = self.U[i][j+1]
            return(x)
        except:
            u = self.U[i][j]
            return(u)



    def expectedValue( self, i, j, a):#, sprime ):
        # print(a, i, j)

        up = self.up(i, j)*.7+ self.down(i, j)*.1+ self.left(i, j)*.1+ self.right(i, j)*.1
        down = self.up(i, j)*.1+ self.down(i, j)*.7+ self.left(i, j)*.1+ self.right(i, j)*.1
        left = self.up(i, j)*.1+ self.down(i, j)*.1+ self.left(i, j)*.7+ self.right(i, j)*.1
        right = self.up(i, j)*.1+ self.down(i, j)*.1+ self.left(i, j)*.1+ self.right(i, j)*.7

        dir = {'^': up,
                'v': down,
                '<': left,
                '>': right}
        reward = dir.get(a)
        return(reward)


    def value_iteration( self ):
        for i in range(1):
            for i in range(len(self.U)):
                for j in range(len(self.U[i])):
                    # self.U[i][j] = self.U[i][j] + self.gama * max(self.expectedValue(i,j,[a for a in self.A]))
                    self.U[i][j] = self.G[i][j] + (self.gama * max(self.expectedValue(i,j,'^'),self.expectedValue(i,j,'v'),self.expectedValue(i,j,'<'),self.expectedValue(i,j,'>')))
                    
    def get_policy( self ):
        print(self.U)
        for i in range(len(self.U)):
            dic = {}
            row = []
            for j in range(len(self.U[i])):
                dic.update({'^' :self.up(i, j)})
                dic.update({'<' :self.left(i, j)})
                dic.update({'>' :self.right(i, j)})
                dic.update({'v' :self.down(i, j)})
                x = max(dic, key=dic.get)
                row.append(x)
            self.policy.append(row)
        return(self.policy)


list = [[0,0,10],
        [0,-1,0],
        [0,-1,0]]


M = MDP(list)
M.value_iteration()
print( M.get_policy() )
