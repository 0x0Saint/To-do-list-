import os

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def remove_task(task):
    for t in tasks:
        if t["task"] == task:
            tasks.remove(t)
            break

def mark_task_completed(task):
    for t in tasks:
        if t["task"] == task:
            t["completed"] = True
            break

def display_tasks():
    for i, t in enumerate(tasks, start=1):
        status = "✓" if t["completed"] else " "
        print(f"{i}. [{status}] {t['task']}")

def save_tasks(file_name):
    with open(file_name, "w") as file:
        for t in tasks:
            file.write(f"{t['task']},{str(t['completed'])}\n")

def load_tasks(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                task, completed = line.strip().split(",")
                tasks.append({"task": task, "completed": completed.lower() == "true"})

# Example usage
load_tasks("tasks.txt")
add_task("Buy groceries")
add_task("Do laundry")
add_task("Clean the house")
display_tasks()
mark_task_completed("Do laundry")
display_tasks()
remove_task("Clean the house")
display_tasks()
save_tasks("tasks.txt")
