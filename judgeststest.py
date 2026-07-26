from datasets import load_dataset
from scipy import stats
from Ais import *

LLama_scores = [5.0, 87.0, 8.0, 73.0, 8.0, 8.0, 8.0, 8.0, 73.0, 8.0, 0.0, 8.0, 8.0, 4.0, 73.0, 0.0, 8.0, 8.0, 8.0, 8.0, 73.0, 73.0, 5.0, 8.0, 8.0, 8.0, 6.0, 0.0, 8.0, 0.0, 2.0, 8.0, 5.0, 6.0, 0.0, 0.0, 5.0, 70.0, 87.0, 8.0, 8.0, 5.0, 73.0, 8.0, 0.0, 87.0, 8.0, 0.0, 8.0, 73.0, 87.0, 5.0, 5.0, 73.0, 0.0, 8.0, 0.0, 8.0, 87.0, 5.0, 5.0, 8.0, 73.0, 8.0, 8.0, 12.0, 73.0, 12.0, 8.0, 0.0, 87.0, 8.0, 8.0, 8.0, 87.0, 73.0, 73.0, 95.0, 8.0, 75.0, 8.0, 73.0, 87.0, 73.0, 73.0, 87.0, 73.0, 0.0, 73.0, 85.0, 87.0, 8.0, 8.0, 87.0, 5.0, 8.0, 4.0, 8.0, 8.0, 87.0, 87.0, 0.0, 8.0, 0.0, 8.0, 4.0, 73.0, 71.0, 73.0, 87.0, 5.0, 5.0, 8.0, 8.0, 8.0, 87.0, 87.0, 87.0, 87.0, 87.0, 87.0, 87.0, 87.0, 87.0, 8.0, 87.0, 87.0, 87.0, 87.0, 87.0, 73.0, 87.0, 87.0, 87.0, 74.0, 34.0, 87.0, 87.0, 5.0, 87.0, 85.0, 95.0, 87.0, 73.0, 87.0, 8.0, 74.0, 87.0, 4.0, 68.0, 8.0, 87.0, 73.0, 8.0, 70.0, 87.0, 73.0, 8.0, 8.0, 79.0, 8.0, 87.0, 87.0, 5.0, 8.0, 87.0, 74.0, 87.0, 8.0, 0.0, 73.0, 8.0, 75.0, 87.0, 87.0, 87.0, 87.0, 73.0, 87.0, 87.0, 87.0, 87.0, 87.0, 95.0, 87.0, 73.0, 73.0, 5.0, 85.0, 87.0, 8.0, 87.0, 5.0, 6.0, 85.0, 22.0, 87.0]
LLama_scaled = [1.15, 3.61, 1.24, 3.19, 1.24, 1.24, 1.24, 1.24, 3.19, 1.24, 1.0, 1.24, 1.24, 1.12, 3.19, 1.0, 1.24, 1.24, 1.24, 1.24, 3.19, 3.19, 1.15, 1.24, 1.24, 1.24, 1.18, 1.0, 1.24, 1.0, 1.06, 1.24, 1.15, 1.18, 1.0, 1.0, 1.15, 3.1, 3.61, 1.24, 1.24, 1.15, 3.19, 1.24, 1.0, 3.61, 1.24, 1.0, 1.24, 3.19, 3.61, 1.15, 1.15, 3.19, 1.0, 1.24, 1.0, 1.24, 3.61, 1.15, 1.15, 1.24, 3.19, 1.24, 1.24, 1.36, 3.19, 1.36, 1.24, 1.0, 3.61, 1.24, 1.24, 1.24, 3.61, 3.19, 3.19, 3.85, 1.24, 3.25, 1.24, 3.19, 3.61, 3.19, 3.19, 3.61, 3.19, 1.0, 3.19, 3.55, 3.61, 1.24, 1.24, 3.61, 1.15, 1.24, 1.12, 1.24, 1.24, 3.61, 3.61, 1.0, 1.24, 1.0, 1.24, 1.12, 3.19, 3.13, 3.19, 3.61, 1.15, 1.15, 1.24, 1.24, 1.24, 3.61, 3.61, 3.61, 3.61, 3.61, 3.61, 3.61, 3.61, 3.61, 1.24, 3.61, 3.61, 3.61, 3.61, 3.61, 3.19, 3.61, 3.61, 3.61, 3.22, 2.02, 3.61, 3.61, 1.15, 3.61, 3.55, 3.85, 3.61, 3.19, 3.61, 1.24, 3.22, 3.61, 1.12, 3.04, 1.24, 3.61, 3.19, 1.24, 3.1, 3.61, 3.19, 1.24, 1.24, 3.37, 1.24, 3.61, 3.61, 1.15, 1.24, 3.61, 3.22, 3.61, 1.24, 1.0, 3.19, 1.24, 3.25, 3.61, 3.61, 3.61, 3.61, 3.19, 3.61, 3.61, 3.61, 3.61, 3.61, 3.85, 3.61, 3.19, 3.19, 1.15, 3.55, 3.61, 1.24, 3.61, 1.15, 1.18, 3.55, 1.66, 3.61]

sts22_en = load_dataset("mteb/sts22-crosslingual-sts", "en")
test_df = sts22_en["test"].to_pandas()
human = test_df["score"].to_list()

def getcorrelation(human_scores, judge_scores):
    rho, p = stats.spearmanr(human_scores, judge_scores)
    return {"rho": rho, "p": p}

def scaletohuman(scores: float) -> float:
    scores = scores/100 * 3 + 1
    scores = round(scores, 2)
    return scores


def sts_test(ai: str):
    original_resp = []
    judge_resp = []
    for i in range(len(test_df)):
        baseline = test_df.iloc[i]["sentence1"]
        res = test_df.iloc[i]["sentence2"]
        original_resp.append(judge(baseline=baseline,res=res))
        judge_resp.append(scaletohuman(original_resp[-1]))

    with open(f'{ai}_STS22.txt', 'a') as s:
        s.write(f'{ai} = {judge_resp}')

    with open(f'{ai}_STS22scaled.txt', 'a') as s:
        s.write(f'{ai}scaled = {original_resp}')

    result = getcorrelation(human,judge_resp)
    return result     

def scaling(scores: list[int], ai: str):
    judge_scores = []
    for i in range(len(scores)):
        judge_scores.append(scaletohuman(scores[i]))

    with open(f'{ai}_STS22scaled.txt', 'a') as s:
        s.write(f'{ai}scaled = {judge_scores}')
    return judge_scores


print(getcorrelation(human,LLama_scores))
print(getcorrelation(human,LLama_scaled))


# Citation
citation = """@inproceedings{chen-etal-2022-semeval,
  address = {Seattle, United States},
  author = {Chen, Xi  and
Zeynali, Ali  and
Camargo, Chico  and
Fl{\"o}ck, Fabian  and
Gaffney, Devin  and
Grabowicz, Przemyslaw  and
Hale, Scott  and
Jurgens, David  and
Samory, Mattia},
  booktitle = {Proceedings of the 16th International Workshop on Semantic Evaluation (SemEval-2022)},
  doi = {10.18653/v1/2022.semeval-1.155},
  editor = {Emerson, Guy  and
Schluter, Natalie  and
Stanovsky, Gabriel  and
Kumar, Ritesh  and
Palmer, Alexis  and
Schneider, Nathan  and
Singh, Siddharth  and
Ratan, Shyam},
  month = jul,
  pages = {1094--1106},
  publisher = {Association for Computational Linguistics},
  title = {{S}em{E}val-2022 Task 8: Multilingual news article similarity},
  url = {https://aclanthology.org/2022.semeval-1.155},
  year = {2022},
}"""