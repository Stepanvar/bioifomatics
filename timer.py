from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import random
import winsound
print("enter number of cycles")
i = int(input())
index = 0
count_z = []
len = i + 1
y = []
while len > 0:
    count_z.append(0)
    len -= 1
while i > 0:
    begin = datetime.now()
    till_two_minutes = begin + timedelta(minutes=2)
    while datetime.now() < till_two_minutes:
        j = 0
    winsound.Beep(random.randint(300,500),1000)
    print("that's all number", i)
    y.append(till_two_minutes)
    file = open("D:/bioinfo/define.txt", encoding = 'utf-8')
    try:
        while True:
            sym = file.read(1)
            if sym == "Z":
                count_z[index] += 1
            elif sym == "":
                break
    finally:
        file.close()
    sent = []
    sent.append(count_z[index] - count_z[index - 1])
    print("number of sentences", count_z[index] - count_z[index - 1])
    index += 1
    i-=1
print(count_z)
while index > 0:
    y.append(j)
    j +=1
    index -= 1
plt.plot(y, sent)
plt.show()