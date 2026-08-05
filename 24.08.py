from pathlib import Path

path = Path("test.txt")

def add_task(**kwargs):
    task = dict()
    with path.open("r", encoding="utf-8") as f:
        for i in f.readlines():
            i = i.strip()
            if not i or "," not in i:
                continue
            ls = i.split(",")
            task[ls[0].strip()] = ls[1].strip()
        task[kwargs['title']] = f"{kwargs['status']}"
    with path.open("w", encoding="utf-8") as f:
        for title, status in task.items():
            f.write(f"{title}, {status}\n")


add_task(title = "купить хлеб", status = "в процессе")

add_task(title = "купить хлеб", status = "выполнено")