import re 

with open("input.txt") as input:
    data = input.read()

# first half 

dataList = data.splitlines()
sumOfCumulativeVal = 0
for line in dataList:
    digitsInLine = [char for char in line if char.isdigit()]
    firstDigit = digitsInLine[0]
    lastDigit = digitsInLine[-1]
    cumulativeVal = int(firstDigit + lastDigit)
    sumOfCumulativeVal += cumulativeVal
print(sumOfCumulativeVal) # 55029

# second half
transformedDataList = []
digitsSpelled = 'zero one two three four five six seven eight nine'.split()
sumOfCumulativeVal = 0
for line in dataList:
    for idx, name in enumerate(digitsSpelled):
        if name in line:
            line = line.replace(name, f'{name}{idx}{name}')            
    transformedDataList.append(line)

for line in transformedDataList:
    digitsInLine = [char for char in line if char.isdigit()]
    firstDigit = digitsInLine[0]
    lastDigit = digitsInLine[-1]
    cumulativeVal = int(firstDigit + lastDigit)
    sumOfCumulativeVal += cumulativeVal
print(sumOfCumulativeVal)