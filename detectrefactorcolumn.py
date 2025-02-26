# -*- coding: utf-8 -*-
"""DetectRefactorColumn.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sQpJl2EdY8C6wWI2OucL7D70B47rJjmE
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/commit_analys/

import pandas as pd
target_project = "wikipedia"
file_path = f"{target_project}_ios_commits.csv"
data = pd.read_csv(file_path)

# Define refactor-related keywords for analysis
refactor_keywords = [
    "refactor", "optimize", "clean up", "restructure", "improve readability", "code cleanup", "clean" "simplify", "reduce complexity",
    "rename", "reorganize", "move", "remove unused", "unused", "apply coding standards", "improve performance", "migrate", "extract method",  "replace"
]

# Create a new column for keyword-based classification
data['Refactor'] = data['Message'].str.contains('|'.join(refactor_keywords), case=False, na=False)

# Display the updated DataFrame to review changes
data.head()

data.to_csv(file_path, index=False)

