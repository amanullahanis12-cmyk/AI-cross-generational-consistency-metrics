from globals import *

# This averages the scores that were made in for the sycophancy results after they have been moved to their length preference folder. 
def sycoavgs():
    types = ["0_ZeroShot_Scores.txt", "0Baseline_Scores.txt","1_ZeroShot_Scores.txt", "1Baseline_Scores.txt"]
    # A list of lists. Every first index in list is lower end and every first index in inner list is zero shot score (compared with previus no zer
    # shot answer).
    sycophavg = {"Claude":[[0,0],[0,0]],"OpenAI":[[0,0],[0,0]],"Mistral":[[0,0],[0,0]],"DeepSeek":[[0,0],[0,0]],"QWEN":[[0,0],[0,0]]}
    ans = 0
    count = 0
    for i in range(len(folders)):
        for j in range(len(mainmodels)):
            main = mainmodels[j]
            for t in range(len(types)):
                with open(f'{folders[i]}/Sycophancy/{main}{types[t]}', 'r') as r:
                    for line in r:
                        ans += float(line)
                        count += 1
                    ans = ans / count
                    print(count)
                    if count < 10:
                        print(f'{folders[i]}/Sycophancy/{main}{types[t]}')
                    # If types[t] is the first two indexes of types then the models value at the first index are updated
                    # In other words the three next if statements basically just get the average of semantic simlarity scores for the lower model
                    if t < 2:
                        # if types[t] is the first type in types then the first index of the first model value is updated with a running total
                        # of the semantic simlarities between the zero-shot answer and the context injected answer to the same prompt
                        if t < 1:
                            sycophavg[main][0][0] += ans
                        else:
                        # if types[t] is the second type in types then the second index of the first model value is updated with a running total
                        # of the semantic simlarities between the frontier model's zero-shot answer and the context injected answer to the 
                        # same prompt
                            sycophavg[main][0][1] += ans
                    # This is the same thing as above but this is the average for the medium model
                    else:
                        if t < 3:
                            sycophavg[main][1][0] += ans
                        else:
                            sycophavg[main][1][1] += ans
                    ans = 0
                    count = 0
    for k,v in sycophavg.items():
        ## all running totals are divided by three for all the different length preferences. 
        sycophavg[k][0][0] = sycophavg[k][0][0]/3
        sycophavg[k][0][1] = sycophavg[k][0][1]/3
        sycophavg[k][1][0] = sycophavg[k][1][0]/3
        sycophavg[k][1][1] = sycophavg[k][1][1]/3
    print(sycophavg)

