from Ais import *

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
    addsycophancy()