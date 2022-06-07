file = open('text.txt', 'r')
line = file.read()
stat = []
for i in line:
    if (len(stat) == 0):
        stat.append([1, i])
    else:
        if stat[len(stat) - 1][1] == i:
            stat[len(stat) - 1][0] += 1
        else:
            stat.append([1, i])
file.close()
zipResult = ''
for i in stat:
    zipResult += ''.join(map(str, i))
print(zipResult)

