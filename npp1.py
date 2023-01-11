
print(" "*18 + "-----Laboratory Activity 3 - SJF-----")

n      = 3
inputs = []
arrtime = 0
tatst  = []
wtst   = []
totalT = 0
totalW = 0

#UI
for a in range(n):
    print(" ")
    job = str(input("Enter the name of the JOB: "))
    at  = int(input("Enter the Arrival Time   : "))
    bt  = int(input("Enter the Burst time     : "))
    prio  = int(input("Enter the Priority     : "))
    inputs.append([job ,at ,bt , prio,"onTemp"])

inputs.sort(key=lambda x: x[1])

#ET
for z in range(n):
    temp1 = []
    temp2 = []
    for x in range(n):
        if inputs[x][1] <= arrtime and inputs[x][3] == "onTemp":
            temp1.append([inputs[x][0],inputs[x][1],inputs[x][2],inputs[x][3]])
        elif inputs[x][3] == "onTemp":
            temp2.append([inputs[x][0],inputs[x][1],inputs[x][2],inputs[x][3]])
    temp1.sort(key=lambda y: (y[3]))
    if len(temp1) >= 1:
        arrtime = arrtime + temp1[0][2]
        for y in range(n):
            if temp1[0][0] == inputs[y][0]:
                break
        inputs[y][3] = "done"
        inputs[y].append(arrtime)
    else:
        temp2.sort(key=lambda y: (y[3]))
        arrtime = arrtime + temp2[0][2]
        for y in range(n):
            if temp2[0][0] == inputs[y][0]:
                break
        inputs[y][3] = "done"
        inputs[y].append(arrtime)

#TAT
for c in range(n):
    arrival = inputs[c][1]
    endtime = inputs[c][4]
    tat = endtime - arrival
    tatst.append(tat)
    totalT = totalT + tatst[c]

#WT
for d in range(n):
    burst = inputs[d][2]
    tat   = tatst[d]
    wt = tat - burst
    wtst.append(wt)
    totalW = totalW + wtst[d]
    
print(" ")
print(" "*18 + "-------------CPU UTILIZATION-------------")
print(" ")
print("| Jobs | Arrival Time | Burst Time | End Time | Turn Around Time | Waiting Time |")
for e in range(n):
    print("|  " + str(inputs[e][0]) + " "*(4-len(inputs[e][0])) + "|      " + str(inputs[e][1]) + " "*(8-len(str(inputs[e][1]))) + "|      " + str(inputs[e][2]) + " "*(6-len(str(inputs[e][2])))
          + "|    " + str(inputs[e][4]) + " "*(6-len(str(inputs[e][4]))) + "|         " + str(tatst[e]) + " "*(9-len(str(tatst[e]))) + "|       " + str(wtst[e]) + " "*(7-len(str(wtst[e]))) + "|")   

aveT = (totalT / n)
aveW = (totalW / n)

print(" ")
print("Total Turn Around Time   : " + str(totalT))
print("Total Waiting Time       : " + str(totalW))
print("Average Turn Around Time : " + str("%.2f" % round(aveT, 2)))
print("Average Waiting Time     : " + str("%.2f" % round(aveW, 2)))

