
str_num = input()

number = [int(i) for i in str_num]
number.sort(reverse=True)

maxScore = number.count(number[0])
midScore = number.count(number[maxScore])
minScore = number.count(number[midScore+maxScore])

gold = []
silver = []
bronze = []
if maxScore > 1:
    if maxScore == 2:
        gold = [number[maxScore-1] for i in range(maxScore)]
        bronze = [number[maxScore]]
    else:
        gold = [number[maxScore-1] for i in range(maxScore)]
else:
    gold = [number[maxScore-1]]
    silver = [number[maxScore]]
    bronze = [number[midScore+maxScore] for i in range(minScore)]
    
print(gold,silver,bronze)