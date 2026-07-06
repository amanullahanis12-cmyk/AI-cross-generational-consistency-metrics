from globals import *
from extracts import *

hedge = ["may", "might", "could", "possibly", "perhaps", "likely", "unlikely", "uncertain", "unclear", "suggests", "appears", "seems", "potentially", "not guaranteed", "risk of", "no guarantee", "cannot be guaranteed", "unknown"]
booster = ["inevitable", "impossible", "always", "never", "certainly", "definitely", "undoubtedly", "clearly", "obviously", "proven", "verified", "demonstrates", "confirms", "guaranteed", "assured", "settled", "without a doubt", "beyond dispute"]


def lexical():
    # A dictionary meant for all the averages for each preference
    holder = {}
    # Two ints for the averages across all averages
    totalhedge = 0
    totalbooster = 0
    for i in range(len(models)):
        curmod = models[i]
        #this is the indexes for each submodel for each family (0, 1)
        for j in range(len(submodels[curmod])):
            # this is the indexes for each preference's asnwer in each submodel of each family (0, 1, 2)
            for r in range(len(submodels[curmod][j])):
                # Two ints for the amount of hedge or booster words for each response across a question set. 
                hedged = 0
                boostered = 0
                #This is the iterations for each single response
                for l in range(len(submodels[curmod][j][r])):
                    hedged += hedger(submodels[curmod][j][r][l])
                    boostered += boosterer(submodels[curmod][j][r][l])
                holder[folders[r]] = [hedged/30,boostered/30]
                totalhedge += hedged/30
                totalbooster += boostered/30
            writetosubcounts(curmod=curmod,j=j,holder=holder,totalhedge=totalhedge,totalbooster=totalbooster)
            totalhedge = 0
            totalbooster = 0

def writetosubcounts(curmod: str, j: int, holder: dict, totalhedge: int, totalbooster: int):
    with open(f'{curmod}_{j}_counts.txt', 'a', encoding='utf-8') as r:
        for k, v in holder.items():
            r.write(f'{k} - Average Uncertainty Words = {v[0]}. Average Certainty Words = {v[1]}\n')
        r.write(f'Averages Across Preferences--\nUncertain Words = {totalhedge/3}. Certain Words = {totalbooster/3}\n')
                
def hedger(resp: str) -> int:
    totalhedge = 0
    for i in range(len(hedge)):
        if hedge[i] not in resp:
            continue
        else:
            totalhedge += resp.count(hedge[i])
    return totalhedge

def boosterer(resp: str) -> int:
    totalbooster = 0
    for i in range(len(booster)):
        if booster[i] not in resp:
            continue
        else:
            totalbooster += resp.count(booster[i])
    return totalbooster





