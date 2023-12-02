with open("input.txt") as input:
    data = input.read()

# part 1
dataList = data.splitlines()
sumOfCumulativeVal = 0
for line in dataList:
    digitsInLine = [char for char in line if char.isdigit()]
    firstDigit = digitsInLine[0]
    lastDigit = digitsInLine[-1]
    cumulativeVal = int(firstDigit + lastDigit)
    sumOfCumulativeVal += cumulativeVal
print(sumOfCumulativeVal) # 55029

# part 2
transformedDataList = []
digitsSpelled = 'zero one two three four five six seven eight nine'.split()
sumOfCumulativeVal = 0
for line in dataList:
    for digit, word in enumerate(digitsSpelled):
        if word in line:
            line = line.replace(word, f'{word}{digit}{word}')            
    transformedDataList.append(line)

for line in transformedDataList:
    digitsInLine = [char for char in line if char.isdigit()]
    firstDigit = digitsInLine[0]
    lastDigit = digitsInLine[-1]
    cumulativeVal = int(firstDigit + lastDigit)
    sumOfCumulativeVal += cumulativeVal
print(sumOfCumulativeVal)