from globals import *

#first index in the list value for each dict is no preference second is medium preference and third is short preference (look at the folders list)
submodelsanswers = {"Claude_0":[], "Claude_1":[],
                    "OpenAI_0":[], "OpenAI_1":[],
                    "Mistral_0":[], "Mistral_1":[],
                    "DeepSeek_0":[], "DeepSeek_1":[],
                    "QWEN_0":[], "QWEN_1":[]}

def extracterno():
   for j in range(len(folders)):
      for i in range(len(mainmodels)):
         oldest = True
         resp = ""
         oldestmodresp = []
         mediummodresp = []
         curmod = mainmodels[i]
         direct = f'{folders[j]}/{curmod} Resp/{curmod}_Responses.txt'
         header0 = f'***{submodels[curmod][0]}*** RESPONSE'
         header1 = f'***{submodels[curmod][1]}*** RESPONSE'
         with open(direct, "r", encoding='utf-8') as r:
            for line in r:
               if line.startswith("PROMPT: <"):
                  continue
               if line.startswith(header0) or line.startswith(header1):
                  line = line[line.index('E')+10:]
               if line.startswith("00000000000000000000000000000000000"):
                  if oldest:
                     oldestmodresp.append(resp)
                     resp = ""
                     oldest = False
                     continue
                  else:
                     mediummodresp.append(resp)
                     resp = ""
                     oldest = True
                     continue
               resp += line
         submodelsanswers[f'{curmod}_0'].append(oldestmodresp)
         submodelsanswers[f'{curmod}_1'].append(mediummodresp)
   submodelrespfilemaker(submodelans=submodelsanswers)

def submodelrespfilemaker(submodelans: dict):
    for k, v in submodelans.items():
       with open(f'{k}.txt', 'a', encoding='utf-8') as s:
          s.write(f'{k} = {v}\n')


def testss():
   allq10shot = [Claude_0, Claude_1, DeepSeek_0, DeepSeek_1, Mistral_0, Mistral_1, OpenAI_0, OpenAI_1, QWEN_0 , QWEN_1]
   for i in range(len((allq10shot))):
      print(len(allq10shot[i]))








