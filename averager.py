from globals import *
import math


# Lower index in each value is the lower model higher index is higher value
submodelfiles = {"Claude":["anthropicclaude-3-haiku","anthropicclaude-sonnet-4.6"],
            "DeepSeek":["deepseek-r11.5b","deepseekdeepseek-v3.2"],
            "Mistral":["ministral-33b","mistralaiministral-14b-2512"],
            "OpenAI":["openaigpt-oss-20b","openaigpt-4o"],
            "QWEN":["qwen30.6b","qwenqwen3.6-plus"]}



def avgss():
    smallerind = 0
    # The count of scores for each submodel file
    count = 0
    #the folowing variable is used to sum the average of each question set within each model
    setcounter = 0
    #running total
    runtotal = 0
    #The following are caches for the scores. The first index is the lower model. The indexes within the inner lists follow the list folders.
    c = [[0,0,0],[0,0,0]]
    d = [[0,0,0],[0,0,0]]
    m = [[0,0,0],[0,0,0]]
    o = [[0,0,0],[0,0,0]]
    q = [[0,0,0],[0,0,0]]
    listoftotalscores = [c,d,m,o,q]
    hold = 0
    for i in range(len(folders)):
        for j in range(len(mainmodels)):
            curmod = mainmodels[j]
            for p in range(len(submodelfiles[curmod])):
                subfile = f'{folders[i]}/{curmod} Resp/{submodelfiles[curmod][p]}.txt'
                with open(subfile, 'r') as r:
                    for line in r:
                        if line == '\n':
                            break
                        count += 1
                        runtotal += float(line)
                        if count % 10 == 0:
                            hold = runtotal - hold
                            listoftotalscores[j][p][smallerind] += hold/10
                            hold = runtotal
                            smallerind += 1
                    #r.write(f'\nTotal Avg.: {runtotal} \n') 
                    
                    runtotal = 0
                    count = 0
                    hold = 0
                    smallerind = 0
    averagers(listoftotalscores)
    

def writescore(subfile: str, avg: float, linenum: int):
    avg = avg / 10
    if linenum == 10:
        title = "Original"
    elif linenum == 20:
        title = "Re-Worded"
    elif linenum == 30:
        title = "Demographic"
    #with open(subfile, 'a') as s:
        #s.write(f'\n{title} Avg.: {avg}\n')
    return avg

def averagers(scores: list):
    for i in range(len(scores)):
        for j in range(len(scores[i])):
            for p in range(len(scores[i][j])):
                scores[i][j][p] = scores[i][j][p] / 3
            scores[i][j].append(sum(scores[i][j])/ len(scores[i][j]))
    print(scores)

def stddev():
    slmmean = 68.35 
    hold = 0
    totalsquaredmean = 0
    for i in range(len(folders)):
        for j in range(len(mainmodels)):
            curmod = mainmodels[j]
            subfile = f'{folders[i]}/{curmod} Resp/{submodelfiles[curmod][0]}.txt'
            sycsubfile = f'{folders[i]}/Sycophancy/{curmod}/{curmod}0Baseline_Scores.txt'
            with open(subfile, 'r') as r:
                for line in r:
                    if line == '\n':
                        break
                    else:
                        hold += 1
                        diff = float(line) - slmmean
                        totalsquaredmean += diff * diff
            with open(sycsubfile) as sc:
                for line in sc:
                    if line == '\n':
                        break
                    else:
                       hold += 1
                       diff = float(line) - slmmean
                       totalsquaredmean += diff * diff
    print(hold) 
    return math.sqrt(totalsquaredmean/ (hold-1))
    


# Sycophancy scroes are still hard coded in medium and short mistral scores
def mistralavg():
    counter = 0
    total,totalcounter = 0, 0
    q1totalaverage,q1counter = 0, 0
    q2totalaverage,q2counter = 0, 0
    q3totalaverage,q3counter = 0, 0
    q4totalaverage,q4counter = 0, 0
    for i in range(len(folders)):
        counter = 0
        if i == 0:
            filetoopen = f'noprefmistralssmall.txt'
        elif i == 1:
            filetoopen = f'mediumprefmistralsmall.txt'
        else:
            filetoopen = f'shortprefmistralsmall.txt'
        with open(filetoopen, 'r') as f:
            for line in f:
                if f == "\n":
                    break
                curscore = float(line)
                if counter < 10:
                    print("q1")
                    q1totalaverage += curscore
                    q1counter += 1
                elif counter < 20:
                    print("q2")
                    q2totalaverage += curscore
                    q2counter += 1
                elif counter < 30:
                    print("q3")
                    q3totalaverage += curscore
                    q3counter += 1
                else: 
                    print("q4")
                    q4totalaverage += curscore
                    q4counter += 1
                total += curscore
                totalcounter += 1
                counter += 1
    print(q1counter)
    print(q2counter)
    print(q3counter)
    print(q4counter)
    print(totalcounter)
    return {"Q1": q1totalaverage/q1counter,
            "Q2": q2totalaverage/q2counter,
            "Q3": q3totalaverage/q3counter,
            "Q4": q4totalaverage/q4counter,
            "Average": total/120}

print(mistralavg())