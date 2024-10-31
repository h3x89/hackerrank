# https://leetcode.com/problems/create-a-dataframe-from-list/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd
from typing import List

# Create a list of lists
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # Create the pandas DataFrame
    df = pd.DataFrame(student_data, columns=['Name', 'Age'])
    return df

print(createDataframe(data))  # Output: 
#      Name  Age
# 0    Alex   10
# 1     Bob   12
# 2  Clarke   13

# Time complexity: O(n)

# How to create virtual environment on osx
# python3 -m venv env
# source env/bin/activate

# how to install pandas
# pip install pandas
