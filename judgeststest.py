from datasets import load_dataset
from scipy import stats
from Ais import *

llama3370b = [8.0, 73.0, 8.0, 73.0, 7.0, 8.0, 8.0, 55.0, 87.0, 8.0, 5.0, 5.0, 8.0, 8.0, 75.0, 0.0, 8.0, 8.0, 8.0, 8.0, 73.0, 82.0, 9.0, 5.0, 5.0, 8.0, 8.0, 0.0, 8.0, 8.0, 5.0, 8.0, 8.0, 6.0, 8.0, 8.0, 8.0, 4.0, 87.0, 8.0, 8.0, 8.0, 73.0, 8.0, 0.0, 87.0, 8.0, 0.0, 8.0, 74.0, 87.0, 8.0, 0.0, 89.0, 5.0, 8.0, 0.0, 8.0, 85.0, 8.0, 6.0, 8.0, 73.0, 8.0, 8.0, 7.0, 73.0, 8.0, 8.0, 8.0, 87.0, 8.0, 8.0, 8.0, 87.0, 75.0, 73.0, 73.0, 8.0, 75.0, 8.0, 73.0, 87.0, 87.0, 73.0, 87.0, 73.0, 8.0, 73.0, 87.0, 87.0, 8.0, 0.0, 86.0, 8.0, 8.0, 8.0, 8.0, 8.0, 87.0, 87.0, 8.0, 8.0, 2.0, 11.0, 8.0, 87.0, 8.0, 73.0, 86.0, 0.0, 5.0, 8.0, 9.0, 8.0, 87.0, 87.0, 87.0, 87.0, 73.0, 73.0, 87.0, 87.0, 87.0, 8.0, 87.0, 87.0, 87.0, 87.0, 87.0, 98.0, 87.0, 87.0, 73.0, 73.0, 34.0, 87.0, 87.0, 5.0, 87.0, 84.0, 87.0, 87.0, 73.0, 98.0, 8.0, 73.0, 87.0, 5.0, 62.0, 5.0, 87.0, 73.0, 8.0, 0.0, 87.0, 73.0, 55.0, 8.0, 87.0, 8.0, 87.0, 87.0, 8.0, 8.0, 87.0, 89.0, 82.0, 74.0, 0.0, 73.0, 8.0, 87.0, 82.0, 87.0, 87.0, 87.0, 73.0, 85.0, 87.0, 87.0, 87.0, 87.0, 95.0, 87.0, 73.0, 87.0, 8.0, 67.0, 87.0, 73.0, 85.0, 8.0, 2.0, 40.0, 25.0, 87.0]
llama3370bscaled = [1.24, 3.19, 1.24, 3.19, 1.21, 1.24, 1.24, 2.65, 3.61, 1.24, 1.15, 1.15, 1.24, 1.24, 3.25, 1.0, 1.24, 1.24, 1.24, 1.24, 3.19, 3.46, 1.27, 1.15, 1.15, 1.24, 1.24, 1.0, 1.24, 1.24, 1.15, 1.24, 1.24, 1.18, 1.24, 1.24, 1.24, 1.12, 3.61, 1.24, 1.24, 1.24, 3.19, 1.24, 1.0, 3.61, 1.24, 1.0, 1.24, 3.22, 3.61, 1.24, 1.0, 3.67, 1.15, 1.24, 1.0, 1.24, 3.55, 1.24, 1.18, 1.24, 3.19, 1.24, 1.24, 1.21, 3.19, 1.24, 1.24, 1.24, 3.61, 1.24, 1.24, 1.24, 3.61, 3.25, 3.19, 3.19, 1.24, 3.25, 1.24, 3.19, 3.61, 3.61, 3.19, 3.61, 3.19, 1.24, 3.19, 3.61, 3.61, 1.24, 1.0, 3.58, 1.24, 1.24, 1.24, 1.24, 1.24, 3.61, 3.61, 1.24, 1.24, 1.06, 1.33, 1.24, 3.61, 1.24, 3.19, 3.58, 1.0, 1.15, 1.24, 1.27, 1.24, 3.61, 3.61, 3.61, 3.61, 3.19, 3.19, 3.61, 3.61, 3.61, 1.24, 3.61, 3.61, 3.61, 3.61, 3.61, 3.94, 3.61, 3.61, 3.19, 3.19, 2.02, 3.61, 3.61, 1.15, 3.61, 3.52, 3.61, 3.61, 3.19, 3.94, 1.24, 3.19, 3.61, 1.15, 2.86, 1.15, 3.61, 3.19, 1.24, 1.0, 3.61, 3.19, 2.65, 1.24, 3.61, 1.24, 3.61, 3.61, 1.24, 1.24, 3.61, 3.67, 3.46, 3.22, 1.0, 3.19, 1.24, 3.61, 3.46, 3.61, 3.61, 3.61, 3.19, 3.55, 3.61, 3.61, 3.61, 3.61, 3.85, 3.61, 3.19, 3.61, 1.24, 3.01, 3.61, 3.19, 3.55, 1.24, 1.06, 2.2, 1.75, 3.61]


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


print(sts_test("Llama"))


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