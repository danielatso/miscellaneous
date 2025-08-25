import os
from datetime import datetime

def make_contribution():

    # New branch
    branch = "b1"
    os.system(f"git checkout -b {branch}")

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S %z")

    with open("data.txt", "a") as file:
        file.write(f'{date}\n')

    # Staging
    os.system("git add data.txt")

    # Commit
    os.system(f'git commit -m "Update data.txt"')

    # Push
    os.system(f"git push --set-upstream origin {branch}")

    # PR
    os.system(f"gh pr create -b 'body' -t 'title'")
    os.system(f"gh pr merge -m")
    os.system(f"git checkout main")
    os.system(f"git branch -d {branch}")
    os.system(f"git push -d origin {branch}")
    os.system(f"git pull")



make_contribution()

