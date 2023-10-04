import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_sal = employee['salary'].sort_values(ascending=False).drop_duplicates()
    return pd.DataFrame({'SecondHighestSalary':[None if sorted_sal.size<2 else sorted_sal.iloc[1]]})
''' 
Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
'''
