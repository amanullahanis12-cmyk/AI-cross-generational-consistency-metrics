from Ais import *
#All Q2 9.2 is question number 10 or index 9 for question set 3 not 2 only lebled diffferent for logic reasons
redo = [1,5,6,7,9,9.2]

# Currenlty only structerd for mistral small 4
def singulartest():
  for f in range(len(folders)):
      baselines = mistralrerun[f]
      for i in range(len(Q1_ChatHistory)):
        quest = []
        for q in range(len(Q1_ChatHistory[i])):

            quest.append(Q1_ChatHistory[i][q].copy())
        if f == 0:
          filename = f'syconoprefmistralssmall'
        elif f == 1:
          quest[2]["content"] = med(quest[2]["content"])
          filename = f'sycomediumprefmistralsmall'
        else:
          quest[2]["content"] = shorted(quest[2]["content"])
          filename = f'sycoshortprefmistralsmall'
        mistralresp = resgenerator("mistralai/mistral-small-2603",quest)
        scores = judge(baselines[i], mistralresp)
        with open(f'{filename}.txt', 'a', encoding='utf-8') as sc, open(f'{filename}resps.txt', 'a', encoding='utf-8') as r:
          sc.write(f'{scores}\n')
          r.write(f'PROMPT: <{quest} >\n')
          r.write(f'***mistralai/mistral-small-2603"*** RESPONSE - {mistralresp}\n0000000000000000000000000000000000000000000000000000000000000000000000000000\n')

def addtest():
  with open("results.txt","a", encoding="utf-8") as r:
    for i in range(len(questions)):
      for q in range(len(questions[i])):
        quest = shorted(questions[i][q])
        r.write(f'Questions Set #{i+1} Question Number {q+1}------------------------------------------------*&\n')
        r.write(f'QUESTION---- {quest}\n')
        r.write(f'{Claudes(quest=quest,questnum=q)}\n')
        r.write(f'{GPTs(quest=quest,questnum=q)}\n')
        r.write(f'{Mistrals(quest=quest,questnum=q)}\n')
        r.write(f'{Deepseeks(quest=quest,questnum=q)}\n')
        r.write(f'{Qwens(quest=quest,questnum=q)}\n')
def addsycophancy():
  with open("ShortPrefSycoPhancyresults.txt","a", encoding="utf-8") as r:
    for i in range(len(Q1_ChatHistory)):
      quest = Q1_ChatHistory[i]
      quest[2]["content"] = shorted(quest[2]["content"] )
      sycochat = f''
      for i in range(len(quest)):
        sycochat += f'{quest[i]["role"]} - {quest[i]["content"]}\n'
      r.write(f'Questions Number #{i+1} ------------------------------------------------*&\n')
      r.write(f'HISTORY/QUESTION---- {sycochat}\n')
      r.write(f'{Claudes(questnum=i,syco=quest)}\n')
      r.write(f'{GPTs(questnum=i,syco=quest)}\n')
      r.write(f'{Mistrals(questnum=i,syco=quest)}\n')
      r.write(f'{Deepseeks(questnum=i,syco=quest)}\n')
      r.write(f'{Qwens(questnum=i,syco=quest)}\n')


if __name__ == "__main__":
    print("hi")

    
