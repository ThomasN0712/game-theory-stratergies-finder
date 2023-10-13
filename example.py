import numpy as np
'''
                Player 2
             ________________
            |10,9  | 11,5   |
Player 1    |7, 7  | 9,4    |
             ---------------
'''
s1= 0
s2= 1
q1= 0
q2= 1
p = np.zeros((2,2,2)) # % set to the number of players and the largest number of strategies
s = {s1, s2}
q = {q1, q2}
player1 = 0
player2 = 1
 

p[player1, s1, q1] = 10
p[player1, s1, q2] = 11
p[player1, s2, q1] = 7
p[player1, s2, q2] = 9
 

p[player2, q1, s1] = 9
p[player2, q1, s2] = 7
p[player2, q2, s1] = 5
p[player2, q2, s2] = 4
 

def isDominated(player, i, set1, set2):
    for j in set1:
        if j != i:
            for k in set2:
                if p[player, i, k] >= p[player, j, k]:
                    return False
    return True

print(isDominated(player2, 1, q, s))