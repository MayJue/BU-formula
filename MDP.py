import random

class MDP():

    def __init__( self, grid ):
        print("init")
        self.G = grid

        ## In this assignment, there is one state per space in the grid.
        ## It is not required that you explicitly represent the states, but
        ## you may.  You are also given the transition probabilities.  Since
        ## the number of states is not constant (we will use different inputs),
        ## you may use a function (stub below) to calculate them.  For instance,
        ## if you start in a state on the left edge of the grid and move left,
        ## your program should realize that the agent should stay in the same
        ## state as a result.  The rewards for your MDP are contained in the
        ## input.

        ## Set of possible actions
        self.A = ['^', 'v', '>', '<']
        self.gama = .99 #gama
        ## An attribute to store state utility values.  You do not have to use
        ## a dictionary, but it helps keep the code clear.
        self.U = []
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[i])):
                row.append(0)
            self.U.append(row)
        for i in self.G:
            print(i)

    def T( self, i, j, a):#, sprime ):
        print(a, i, j)
        try:
            up = {self.G[i+1][j]: 1, self.G[i-1][j]: 7, self.G[i][j+1]: 1, self.G[i][j-1]: 1}
            down = {self.G[i+1][j]: 7, self.G[i-1][j]: 1, self.G[i][j+1]: 1, self.G[i][j-1]: 1}
            left = {self.G[i+1][j]: 1, self.G[i-1][j]: 1, self.G[i][j+1]: 1, self.G[i][j-1]: 7}
            right = {self.G[i+1][j]: 1, self.G[i-1][j]: 1, self.G[i][j+1]: 7, self.G[i][j-1]: 1}
            print(self.G[i-1][j], "G")
            print(i-1, j, self.G[-2][0])
            dir =  {'^': random.choice([x for x in up for y in range(up[x])]),
                    'v': random.choice([x for x in down for y in range(down[x])]),
                    '<': random.choice([x for x in left for y in range(left[x])]),
                    '>': random.choice([x for x in right for y in range(right[x])])}
            print('this is ^', dir.get('^'))
            x = dir.get(a)
            print(x)
            return (x)
        except IndexError as error:
            print('exception ', self.G[i][j])
            return(self.G[i][j])
        # chance = random.randrange(1, 11)
        # if a == '^':
        #     if chance < 8:
        #         try:
        #             return(self.U[i+1][j])
        #         except:
        #             return(self.U[i][j])
        #     elif chance == 8 :
        #         try:
        #             return(self.U[i-1][j])
        #         except:
        #             return(self.U[i][j])
        #     elif chance == 9 :
        #         try:
        #             return(self.U[i][j+1])
        #         except:
        #             return(self.U[i][j])
        #     elif chance == 10 :
        #         try:
        #             return(self.U[i-1][j-1])
        #         except:
        #             return(self.U[i][j])
        # elif a == '<':
        #
        #     return 1
        # elif a == '>':
        #
        #     return 1
        # elif a == 'v':
        #
        #     return 2

        ## Return the probability of moving to state sprime after taking action
        ## a in state s.  If sprime is unreachable from s, return 0.

    def value_iteration( self ):
        print("self")
        for i in range(len(self.U)):
            for j in range(len(self.U[i])):
                # self.U[i][j] = self.U[i][j] + self.gama * max(self.T(self.U[i][j], a for a in self.A))
                self.U[i][j] = self.U[i][j] + self.gama * max(self.T(i,j,'^'),self.T(i,j,'v'),self.T(i,j,'<'),self.T(i,j,'>'))



                #CurrReward + self.gama * max( (T(s, "up", spri)),(T(s, "down", spri)),(T(s, "right", spri)),(T(s, "left", spri)))
        ## The value iteration algorithm.  You may use any value for gamma
        ## between 0 and 1 (typically set to something like 0.99).  The number
        ## of updates to carry out is not fixed, but you must run until the
        ## resulting policy converges and stops changing.  You can do this by
        ## iterating until the utility values stop changing by much.  Usually,
        ## this is accomplished by setting some parameter epsilon (small value,
        ## on the order of .1, .01, etc.), summing up the differences between
        ## state utility values before and after the update, and checking
        ## whether it is less than epsilon.

    def get_policy( self ):
        print(self.U)
        print("policy")
        ## Use the attribute self.U to determine the appropriate policy, and
        ## return a grid the same size as the input

list = [[1,2,3],
        [4,5,6],
        [7,8,9]]

        # [[0,0,10],
        # [0,-1,0],
        # [0,-1,0]]


M = MDP(list)
M.value_iteration()
print( M.get_policy() )
