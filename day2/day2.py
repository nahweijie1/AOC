import re 

with open("input.txt") as input:
    data = input.read().split("\n")

# part 1
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

gameDict = {}

for id, hands in enumerate(data):
     hands = hands.split(':')[1:]
     for hand in hands:
         hand = hand.split(';')
         gameDict[id+1] = hand

possibleIDs = []
for game, hands in gameDict.items():
    redMax = 0
    greenMax = 0
    blueMax = 0
    
    for hand in hands:
        redCount = ''.join(re.findall('(\d*).red', hand))
        redCount = int(redCount) if redCount.isnumeric() else 0
        greenCount = ''.join(re.findall('(\d*).green', hand))
        greenCount = int(greenCount) if greenCount.isnumeric() else 0
        blueCount = ''.join(re.findall('(\d*).blue', hand))
        blueCount = int(blueCount) if blueCount.isnumeric() else 0
            
        if redCount > redMax:
            redMax = redCount
        if greenCount > greenMax:
            greenMax = greenCount
        if blueCount > blueMax:
            blueMax = blueCount
                  
    if (redMax <= MAX_RED and greenMax <=  MAX_GREEN and blueMax <= MAX_BLUE):
        possibleIDs.append(game)

sum = sum(possibleIDs)
print(sum)

# part 2

sum = 0
for game, hands in gameDict.items():
    redMax = 0
    greenMax = 0
    blueMax = 0
    power = 0
    
    for hand in hands:
        redCount = ''.join(re.findall('(\d*).red', hand))
        redCount = int(redCount) if redCount.isnumeric() else 0
        greenCount = ''.join(re.findall('(\d*).green', hand))
        greenCount = int(greenCount) if greenCount.isnumeric() else 0
        blueCount = ''.join(re.findall('(\d*).blue', hand))
        blueCount = int(blueCount) if blueCount.isnumeric() else 0
            
        if redCount > redMax:
            redMax = redCount
        if greenCount > greenMax:
            greenMax = greenCount
        if blueCount > blueMax:
            blueMax = blueCount
        power = redMax * greenMax * blueMax
        
    sum += power  
print(sum)