from globals import *
from generating import *

def base():
    with open("Base.txt","a", encoding="utf-8") as f:
        f.write("\n\n\n")
        for i in range(len(mainmod)):
            hold = mainmod[i]
            names = mainmod[i][0:3] + ".txt"
            with open(names, "a", encoding="utf-8") as b:
                f.write(f'*{hold}* baseline responses\n')
                b.write(f'{hold}base = [')
                for j in range(len(Q1_NoPref)):
                    quest = shorted(Q1_NoPref[j])
                    quest = [{"role":"user","content":quest}]
                    answer = resgenerator(hold, quest)
                    f.write(f'PROMPT # {j}:\n <{quest}> \n')
                    f.write(f'RESPONSE # {j}:\n <{answer}>\n-----------------\n')
                    b.write(f' """{answer}""",\n')
                b.write(f']\n\n')
#base()
