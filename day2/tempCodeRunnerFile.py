possibleIDs = []
# for game, hands in gameDict.items():
#     redMax = 0
#     greenMax = 0
#     blueMax = 0
#     for hand in hands:
#         redCount = ''.join(re.findall('(\d*).red', hand))
#         if redCount.isnumeric():
#             redCount = int(redCount)
#         else:
#             redCount = 0
#         greenCount = ''.join(re.findall('(\d*).green', hand))
#         if greenCount.isnumeric():
#             greenCount = int(greenCount)
#         else:
#             greenCount = 0
#         blueCount = ''.join(re.findall('(\d*).blue', hand))
#         if blueCount.isnumeric():
#             blueCount = int(blueCount)
#         else:
#             blueCount = 0
#         if redCount > redMax:
#             redMax = redCount
#         if greenCount > greenMax:
#             greenMax = greenCount      
#         if blueCount > blueMax:
#             blueMax = blueCount       
#     if (redMax <= MAX_RED and greenMax <=  MAX_GREEN and blueMax <= MAX_BLUE):
#         possibleIDs.append(game)

# sum = sum(possibleIDs)
# print(sum)