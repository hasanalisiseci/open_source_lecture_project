
# if PyGithub not installed run this line
# !pip install PyGithub pandas

from google.colab import drive
import re
from github import Github
import pandas as pd

# Connect Google Drive
drive.mount('/content/my_drive')

personal_token = "{your-personal-github-token}"
token = Github(personal_token)

repo_name = "{your-target-repo-path}"
repo = token.get_repo(repo_name)

commits = repo.get_commits()

commit_data = []


for commit in commits[:999]:
    message = commit.commit.message
    message = message.lower()
    cleaned_message = re.sub(r"\(#\d+\)", "", message).strip()
    commit_data.append([commit.sha, commit.commit.author.name, commit.commit.author.email, commit.commit.author.date, cleaned_message])

df = pd.DataFrame(commit_data, columns=["SHA", "Author Name", "Author Email", "Author Date", "Message"])

refactor_keywords = [
    "refactor",
    "optimize",
    "clean up",
    "restructure",
    "improve readability",
    "code cleanup",
    "clean"
    "simplify",
    "reduce complexity",
    "rename",
    "reorganize",
    "move",
    "remove unused",
    "apply coding standards",
    "improve performance",
    "migrate",
    "extract method",
    "replace"
]

for index, row in df.head(299).iterrows():  # Sadece ilk 100 index için
    message = row["Message"]
    if any(keyword in message for keyword in refactor_keywords):
        df.loc[index, "Refactor"] = True
    else:
        df.loc[index, "Refactor"] = False

%cd /content/my_drive/MyDrive/CSV/

df.to_csv('{yourFileName}.csv', index=False)