file = open("cat logfile.txt", "r")
lines = file.readlines()
file.close()
count= len(lines)
for i in range(0,count):
    lines[i] = lines[i].replace('0:10','')
for i in range(1,len(lines)):
    if i >= count:
        break    
    RepeatedState = lines.count(lines[i])
    print(str(lines[i]).strip() + '\t' + str(RepeatedState))
    for j in range(i+1,count):
        if RepeatedState>1 and (lines[i]==lines[j]):
            lines.pop(j)
            RepeatedState = lines.count(lines[i])
            count = len(lines)
