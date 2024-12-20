# https://leetcode.com/problems/create-a-dataframe-from-list/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

# Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.

# The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.

# The result format is in the following example.

 

# Example 1:

# Input:
# student_data:
# [
#   [1, 15],
#   [2, 11],
#   [3, 11],
#   [4, 20]
# ]
# Output:
# +------------+-----+
# | student_id | age |
# +------------+-----+
# | 1          | 15  |
# | 2          | 11  |
# | 3          | 11  |
# | 4          | 20  |
# +------------+-----+
# Explanation:
# A DataFrame was created on top of student_data, with two columns named student_id and age.

import pandas as pd
from typing import List

# Create a list of lists
data = [[1, 15], [2, 11], [3, 11], [4, 20]]

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # Create the pandas DataFrame
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

# print(createDataframe(data))  # Output:
#   student_id  age
# 0           1   15
# 1           2   11
# 2           3   11
# 3           4   20

# print()


print('+------------+-----+')
print('| student_id | age |')
print('+------------+-----+')
df = createDataframe(data)
print(df.to_string(
    index=False,
    header=False,
    justify='left',
    formatters={
        'student_id': lambda x: f'| {x:<10}',
        'age': lambda x: f'| {x:<3} |'
    }
))
print('+------------+-----+')

# Output:
# +------------+-----+
# | student_id | age |
# +------------+-----+
# | 1          | 15  |
# | 2          | 11  |
# | 3          | 11  |
# | 4          | 20  |
# +------------+-----+