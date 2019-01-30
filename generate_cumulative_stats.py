import ast
import math
head = 40
filename = "cue_stats.txt"
file = open(filename, "r")
cue_stats = ast.literal_eval(file.readline())
cue_summary = []
for cue in cue_stats:
    pauses = []
    for info_set in cue_stats[cue]:
        for pause in info_set[1]:
            pauses.append(pause)
    total = 0
    count = 0
    for pause in pauses:
        total += pause
        count += 1
    if len(pauses) == 0:
        average = 0
        cue_summary.append([cue,average,count,0])
    else:
        average = total / float(count)
        cue_summary.append([cue,average,count,math.log(count)*average])
count = 0
cue_summary = sorted(cue_summary, key=lambda x: x[3], reverse=True)
for cue in cue_summary:
    if count < head:
        print("{0:20.20} Avg: {1:3.2f} n={2}".format(cue[0],cue[1],cue[2]))
        count += 1
