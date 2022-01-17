## Nathan Hinton
## This program should load and save the game state for further opening.

def saveData(filepath, chickens, stats):
    data = ""
    for item in stats:
        data += str(item) + "\n"
    for chicken in chickens:
        data += "chicken: %s, %s, %s, %s, %s, %s, %s\n"%(int(chicken.x), int(chicken.y), int(chicken.food), int(chicken.hydration), chicken.speed, chicken.foodMax, chicken.hydrationMax)
    with open(filepath, 'w') as file:
        file.write(data)

from chicken import Chicken

def loadData(filepath, screen, chickenImage, gameQueue):
    try:
        with open(filepath, 'r') as file:
            data = file.read()
        chickens = []
        stats = []
        for line in data.split('\n'):
            if "chicken: " in line: #if the line contains a chicken:
                line = line.replace('chicken: ', '')
                line = line.split(', ')
                tmp = Chicken(screen, chickenImage, gameQueue, x = int(line[0]), y = int(line[1]))
                tmp.food = int(line[2])
                tmp.hydration = int(line[3])
                tmp.speed = int(line[4])
                tmp.foodMax = int(line[5])
                tmp.hydrationMax = int(line[6])
                chickens.append(tmp)
            elif line == '':
                pass
            else:
                try:
                    stats.append(int(line))
                except ValueError:
                    stats.append(float(line))
        return (chickens, stats)
    except FileNotFoundError:
        return []


"""
fileFormat:

eggs: (count)
chicken: (information)
chicken: (information)
chicken: (information)
...


"""
