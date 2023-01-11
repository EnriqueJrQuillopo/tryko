print("Non-Preemptive")
numberjobs = 5
jobs = []
wt = []
tat = []
current = 0

for i in range(numberjobs):
    name = input("Enter Name of the Job: ")
    ar = int(input("Enter Arrival time of job " + name + ": "))
    br = int(input("Enter Burst Time of job " + name + ": "))
    prio = int(input("Enter Priority of job " + name + ": "))
    jobs.append([name, ar, br, prio, False])

jobs.sort(key=lambda x: (x[1]))

for j in range(numberjobs):
    toprocess = []
    queue = []
    for k in range(numberjobs):
        if jobs[k][1]<=current and jobs[k][4]==False:
            toprocess.append([jobs[k][0],jobs[k][1],jobs[k][2], jobs[k][3]])
        elif jobs[k][4] == False:
            queue.append([jobs[k][0],jobs[k][1],jobs[k][2], jobs[k][3]])
    if len(toprocess)!=0:
        toprocess.sort(key=lambda x : (x[3]))
        current = current + toprocess[0][2]
        for g in range(numberjobs):
            if toprocess[0][0] == jobs[g][0]:
                break
        jobs[g][4] = True
        jobs[g].append(current)
    elif len(toprocess)==0:
        queue.sort(key=lambda x : (x[1], x[3]))
        if current < queue[0][1]:
            current = queue[0][1]
        current = current + queue[0][2]
        for q in range(numberjobs):
            if jobs[q][0] == queue[0][0]:
                break
        jobs[q][4] = True
        jobs[q].append(current)

totalturn = 0
totalwt =0
for c in range(numberjobs):
    et = jobs[c][5]
    at = jobs[c][1]
    turn = et - at
    tat.append(turn)
    totalturn = totalturn + turn


for h in range(numberjobs):
    turn = tat[h]
    bt = jobs[h][2]
    wait = turn - bt
    wt.append(wait)
    totalwt = totalwt + (wait)

print("J     AT     BT     P     TAT    WT")
for r in range(numberjobs):
    print(jobs[r][0] + "     " + str(jobs[r][1]) + "     " + str(jobs[r][2]) + "     " + str(jobs[r][3]) + "     " + str(tat[r]) + "     " + str(wt[r]))

avetat = float(totalturn / numberjobs)
avewt = float(totalwt / numberjobs)
print("AVERAGE TURN AROUND TIME : " + str(avetat))
print("AVERAGE WAITING TIME : " + str(avewt))

        