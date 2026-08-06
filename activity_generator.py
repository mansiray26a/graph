import os
from datetime import datetime
import time

NUM_COMMITS = 5

for i in range(NUM_COMMITS):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("activity.txt", "a", encoding="utf-8") as f:
        f.write(f"Real update at {timestamp}\n")

    os.system("git add activity.txt")
    os.system(f'git commit -m "Update activity #{i+1}"')

    time.sleep(2)

print(f"{NUM_COMMITS} commits created.")