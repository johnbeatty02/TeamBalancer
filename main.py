#To Do List:
#make .exe file
#drag teams in .txt
#integrate google docs
#autogenerate team pictures (discord api), Pillow (PIL) library

#Export team pictures to folders for easier image creation
#https://note.nkmk.me/en/python-pillow-paste/

#Upload images to johnbeatty.net


import random #DAQ
import numpy as np
l1 = random.randint(1,200)
l2 = random.randint(1,200)
l3 = random.randint(1,200)
l4 = random.randint(1,200)
l5 = random.randint(1,200)
l6 = random.randint(1,200)
l7 = random.randint(1,200)
l8 = random.randint(1,200)
l9 = random.randint(1,200)
l10 = random.randint(1,200)
l11 = random.randint(1,200)
l12 = random.randint(1,200)
l13 = random.randint(1,200)
l14 = random.randint(1,200)
l15 = random.randint(1,200)
l16 = random.randint(1,200)

levels = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16]
players = np.genfromtxt('players.txt',dtype='str')
playerLevels = zip(players, levels)
playerLevelsList = list(playerLevels)

averageLevels = sum(levels)/len(levels)
print('Average level is', averageLevels)

import binpacking
bins = binpacking.to_constant_bin_number(playerLevelsList, 4, 1)

a, b, c, d = [ [individualArray] for individualArray in bins]

a = a[0]
b = b[0]
c = c[0]
d = d[0]
a1 = a[1]
b1 = b[1]
c1 = c[1]
d1 = d[1]

team1 = list(zip(*a))
team2 = list(zip(*b))
team3 = list(zip(*c))
team4 = list(zip(*d))

points1 = sum(team1[1])/4
points2 = sum(team2[1])/4
points3 = sum(team3[1])/4
points4 = sum(team4[1])/4

stdev1 = np.std(team1[1])
stdev2 = np.std(team2[1])
stdev3 = np.std(team3[1])
stdev4 = np.std(team4[1])

print('Team 1 is', team1[0], 'and has an average of', points1, 'and a standard deviation of', stdev1)
print('Team 2 is', team2[0], 'and has an average of', points2, 'and a standard deviation of', stdev2)
print('Team 3 is', team3[0], 'and has an average of', points3, 'and a standard deviation of', stdev3)
print('Team 4 is', team4[0], 'and has an average of', points4, 'and a standard deviation of', stdev4)
print('\n-----Stats-----')
