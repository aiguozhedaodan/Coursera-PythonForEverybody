import re
count = 0
total = 0
file = open("regex_sum_188956.txt")
for line in file:
    word = re.findall('[0-9]+',line)
    for words in word:
        num=int(words)
        count = count +1
        total = total + num
avg = total/count
print(total,count,avg)
