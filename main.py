from Ais import *
#All Q2 9.2 is question number 10 or index 9 for question set 3 not 2 only lebled diffferent for logic reasons
redo = [1,5,6,7,9,9.2]

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
  with open("Med_Prefresults.txt","a", encoding="utf-8") as r:    
    for q in range(len(redo)):
      #Change this to quest = questions[i][q]
      #delete next line regardless and all the logic until r.write. should b only quest = questions[i][q]
      questss = redo[q]
      # Verify in responses that the last question in Q3 ia being asked
      if questss == 9.2:
        questss = 9
        quest = med(questions[2][questss])
      else:
        quest = med(questions[1][questss])
      r.write(f'Questions Set #{q+1} Question Number {q+1}------------------------------------------------*&\n')
      r.write(f'QUESTION---- {quest}\n')
      r.write(f'{Claudes(quest=quest,questnum=questss)}\n')
      r.write(f'{GPTs(quest=quest,questnum=questss)}\n')
      r.write(f'{Mistrals(quest=quest,questnum=questss)}\n')
      r.write(f'{Deepseeks(quest=quest,questnum=questss)}\n')
      r.write(f'{Qwens(quest=quest,questnum=questss)}\n')

def addsycophancy():
  #BEFORE RUNNING MAKE SURE IN AIS MODELSELECTION() IS CORRECT WHEN SELECTiNG THE INNER LIST FROM THE ALL RESPONSES FILE AND THE LINE HERE 
  # Also change the base in globals for the frontier model
  with open("ShortPrefSycoPhancyresults.txt","a", encoding="utf-8") as r:
    for i in range(len(Q1_ChatHistory)):
      quest = Q1_ChatHistory[i]
      quest[2]["content"] = shorted(quest[2]["content"])
      sycochat = f''
      for j in range(len(quest)):
        sycochat += f'{quest[j]["role"]} - {quest[j]["content"]}\n'
      r.write(f'Questions Number #{i+1} ------------------------------------------------*&\n')
      r.write(f'HISTORY/QUESTION---- {sycochat}\n')
      r.write(f'{Claudes(questnum=i,syco=quest)}\n')
      r.write(f'{GPTs(questnum=i,syco=quest)}\n')
      r.write(f'{Mistrals(questnum=i,syco=quest)}\n')
      r.write(f'{Deepseeks(questnum=i,syco=quest)}\n')
      r.write(f'{Qwens(questnum=i,syco=quest)}\n')


if __name__ == "__main__":
    singulartest()

    
