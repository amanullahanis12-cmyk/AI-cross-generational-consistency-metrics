from globals import *
from extracts import *

hedge = ["may", "might", "could", "possibly", "perhaps", "unlikely", "uncertain", "unclear", "suggests", "seems", "potentially", "unknown", "not guaranteed", "no guarantee", "cannot be guaranteed", "presumably", "somewhat"]
booster = ["inevitable", "always", "certainly", "undoubtedly", "clearly", "obviously", "demonstrates", "confirms", "assured", "without a doubt", "beyond dispute", "unquestionably", "absolutely", "evidently", "indisputably", "unambiguous", "with certainty"]

#Basically this program just gets the counts of every word in the list for each response than makes an average accross all and all the different
# pref. 
#You have to fix this

def lexical(submodels):
    # A dictionary meant for all the averages for each preference
    #Every first index in each tuple is the uncertainty count and second index is certainty count
    #Every first tuple element in each list value is lower model and second tuple is medium model
    holder = {"Claude":[(),()],
              "DeepSeek":[(),()],
              "Mistral":[(),()],
              "OpenAI":[(),()],
              "QWEN":[(),()]}
    # Two ints for the averages across all averages
    totalhedge = 0
    totalbooster = 0
    #for every answer list
    for i in range(len(submodels)):
        hold = i
        # this is to make sure that index for mainmodels match and is not bigger than mainmodels size
        if hold >= 10:
            hold -= 10
        if hold % 2 == 0:
            whichsubmodel = 0
            curmod = mainmodels[hold//2]
        else:
            whichsubmodel = 1
            curmod = mainmodels[(hold-1)//2]
        #for every length preference
        for r in range(len(submodels[i])):
            # Two ints for the amount of hedge or booster words for each response across a question set. 
            hedged = 0
            boostered = 0
            #For every response within each preference
            for l in range(len(submodels[i][r])):
                hedged += hedger(submodels[i][r][l])
                boostered += boosterer(submodels[i][r][l])
            totalhedge += hedged
            totalbooster += boostered
        if not holder[curmod][whichsubmodel]: holder[curmod][whichsubmodel] = (totalhedge,totalbooster)
        else: holder[curmod][whichsubmodel] = ((holder[curmod][whichsubmodel][0]+totalhedge)/120,
                                               (holder[curmod][whichsubmodel][1]+totalbooster)/120)
        totalhedge = 0
        totalbooster = 0
    return holder

def writetosubcounts(curmod: str, j: int, holder: dict, totalhedge: int, totalbooster: int):
    with open(f'{curmod}_{j}_counts.txt', 'a', encoding='utf-8') as r:
        for k, v in holder.items():
            r.write(f'{k} - Average Uncertainty Words = {v[0]}. Average Certainty Words = {v[1]}\n')
        r.write(f'Averages Across Preferences--\nUncertain Words = {totalhedge/3}. Certain Words = {totalbooster/3}\n')
                
def hedger(resp: str) -> int:
    totalhedge = 0
    for i in range(len(hedge)):
        alt = hedge[i].capitalize()
        if hedge[i] not in resp and alt not in resp:
            continue
        else:
            totalhedge += resp.count(hedge[i])
            totalhedge += resp.count(alt)
    return totalhedge

def boosterer(resp: str) -> int:
    totalbooster = 0
    for i in range(len(booster)):
        alt = booster[i].capitalize()
        if booster[i] not in resp and alt not in resp:
            continue
        else:
            totalbooster += resp.count(booster[i])
            totalbooster += resp.count(alt)
    return totalbooster

print(lexical(submodels=submodsanswers))

