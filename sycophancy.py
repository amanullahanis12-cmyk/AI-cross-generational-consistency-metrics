from globals import *

def sycoavgs():
    types = ["0_ZeroShot_Scores.txt", "0Baseline_Scores.txt","1_ZeroShot_Scores.txt", "1Baseline_Scores.txt"]
    # A list of tuples. Every first index in list is lower end and every first index in tuple is zero shot score (compared with previus no zer
    # shot answer).
    sycophavg = {"Claude":[[0,0],[0,0]],"OpenAI":[[0,0],[0,0]],"Mistral":[[0,0],[0,0]],"DeepSeek":[[0,0],[0,0]],"QWEN":[[0,0],[0,0]]}
    ans = 0
    count = 0
    for i in range(len(folders)):
        for j in range(len(models)):
            for t in range(len(types)):
                with open(f'{folders[i]}/Sycophancy/{models[j]}{types[t]}', 'r') as r:
                    for line in r:
                        ans += float(line)
                        count += 1
                    ans = ans / count
                    print(count)
                    if count < 10:
                        print(f'{folders[i]}/Sycophancy/{models[j]}{types[t]}')
                    if t < 2:
                        if t < 1:
                            sycophavg[models[j]][0][0] += ans
                        else:
                            sycophavg[models[j]][0][1] += ans
                    else:
                        if t < 3:
                            sycophavg[models[j]][1][0] += ans
                        else:
                            sycophavg[models[j]][1][1] += ans
                    ans = 0
                    count = 0
    for k,v in sycophavg.items():
        sycophavg[k][0][0] = sycophavg[k][0][0]/3
        sycophavg[k][0][1] = sycophavg[k][0][1]/3
        sycophavg[k][1][0] = sycophavg[k][1][0]/3
        sycophavg[k][1][1] = sycophavg[k][1][1]/3
    print(sycophavg)
