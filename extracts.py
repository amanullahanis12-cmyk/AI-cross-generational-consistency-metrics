from globals import *
from allrespssubmods import *

#first index in the list value for each dict is no preference second is medium preference and third is short preference (look at the folders list)
submodelsanswers = {"Claude_0":[], "Claude_1":[],
                    "OpenAI_0":[], "OpenAI_1":[],
                    "Mistral_0":[], "Mistral_1":[],
                    "DeepSeek_0":[], "DeepSeek_1":[],
                    "QWEN_0":[], "QWEN_1":[]}

# This program basically just gets the responses from the differnt foldes and makes three list for each model. Each list is a differnet pref. 
def extracterno(syco=False):
   respiscomiing = False
   for j in range(len(folders)):
      for i in range(len(mainmodels)):
         oldest = True
         resp = ""
         oldestmodresp = []
         mediummodresp = []
         curmod = mainmodels[i]
         if syco:
            direct = f'{folders[j]}/Sycophancy/{curmod}/{curmod}_Responses.txt'   
         else:
            direct = f'{folders[j]}/{curmod} Resp/{curmod}_Responses.txt'
         header0 = f'***{submodelscodes[curmod][0]}*** RESPONSE'
         header1 = f'***{submodelscodes[curmod][1]}*** RESPONSE'
         with open(direct, "r", encoding='utf-8') as r:
            for line in r:
               if line.startswith(header0) or line.startswith(header1):
                  line = line[line.index('E')+10:]
                  respiscomiing = True
               if line.startswith("0000000000000000000000000000000000000000000000000000000000000000000000000000"):
                  if oldest:
                     oldestmodresp.append(resp)
                     resp = ""
                     oldest = False
                     respiscomiing = False
                     continue
                  else:
                     mediummodresp.append(resp)
                     resp = ""
                     oldest = True
                     respiscomiing = False
                     continue
               if respiscomiing:
                  resp += line
         submodelsanswers[f'{curmod}_0'].append(oldestmodresp)
         submodelsanswers[f'{curmod}_1'].append(mediummodresp)
   submodelrespfilemaker(submodelans=submodelsanswers)

def submodelrespfilemaker(submodelans: dict):
    for k, v in submodelans.items():
       with open(f'{k}.txt', 'a', encoding='utf-8') as s:
          s.write(f'{k} = {v}\n')
       with open(f'AllResp.txt', 'a', encoding='utf-8') as f:
          f.write(f'{k} = {v}\n')


def testss():
   for i in range(len((submodsanswers))):
      holder = ""
      for j in range(len(submodsanswers[i])):
         holder += f'{len(submodsanswers[i][j])}, '
      print(f'{holder}\n')

def printquestions():
   with open("printed_questions_no_pref.txt",'a', encoding='utf-8') as p:
      for i in range(len(Q1_NoPref)):
         p.write(f'Question # {i+1}: \n')
         p.write("Q1: "+Q1_NoPref[i]+'\n')
         p.write("Q2: "+Q2_NoPref[i]+'\n')
         p.write("Q3: "+Q3_NoPref[i]+'\n')
         p.write("Questions With History: \n")
         for j in range(len(Q1_ChatHistory[i])):
            p.write(f'{Q1_ChatHistory[i][j]["role"]}: {Q1_ChatHistory[i][j]["content"]}\n')

def adding(files,responses, responseprefind):
   hold = 0
   resp = ""
   for line in files:
      if line.startswith("0000000000000000000000000000000000000000000000000000000000000000000000000000"):
         responses[responseprefind][hold] = resp
         resp = ""
         hold += 1
         continue
         
      if line.startswith("***mistralai/mistral-small-2603"):
         line = line[line.index('E')+10:]
      
      if line.startswith("PROMPT: <"):
         continue
      resp += line

def mistralextr():
   for i in range(len(folders)):
      
      if i == 0:
         filetoopen = f'noprefmistralssmallresps.txt'
      elif i == 1:
         filetoopen = f'mediumprefmistralsmallresps.txt'
      else:
         filetoopen = f'shortprefmistralsmallresps.txt'

      with open(filetoopen, 'r', encoding='utf-8') as f:
         adding(f, Mistral_1, i)
      with open(f'syco{filetoopen}', 'r', encoding='utf-8') as r:
         adding(r, Mistral_1syco, i)
   with open(f'All Responses/Mistral_1.txt', 'w', encoding='utf-8') as m:
      m.write(f'Mistral_1 = {Mistral_1}')
   with open(f'Sycophancy Results/Mistral/Mistral_1.txt', 'w', encoding='utf-8') as ms:
      ms.write(f'Mistral_1syco = {Mistral_1syco}')
      
   print(Mistral_1)
   print(Mistral_1syco)

#testss()