players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])# 将打印前三个值 ['charles', 'martina', 'michael']
print(players[1:4])# 将打印索引为1，2，3的值，包含头不包尾 ['martina', 'michael', 'florence']
print(players[:4])#没有指定起始，则从头开始打印 ['charles', 'martina', 'michael', 'florence']
print(players[2:])#将从索引为2处开始打印，直到结尾 ['michael', 'florence', 'eli']
print(players[-3:])#将打印倒数第三个至最后一个，即最后三个 ['michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:# 遍历切片
    print(player.title())
