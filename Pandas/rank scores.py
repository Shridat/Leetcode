import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    if scores.shape[0]==0:
        return pd.DataFrame({'score':[],'rank':[]})
    scores = scores.sort_values(by="score",ascending=False)

    rank =[1]
    j = 1
    prev = scores['score'].iloc[0]

    for i in scores['score'].iloc[1:]:
        if i!=prev:
            j+=1
        rank.append(j)
        prev = i
    scores['rank'] = rank
    return scores[['score','rank']]
''' 
Example 1:

Input: 
Scores table:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
Output: 
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
'''
