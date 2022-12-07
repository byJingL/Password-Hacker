# 2022.12.4
class Task:
    def __init__(self, description, team):
        self.description = description
        self.team = team

    def __add__(self, other):
        self.description = self.description +'\n'+other.description
        self.team = f'{self.team}, {other.team}'
        return Task(self.description, self.team)

task1 = Task("Finish the assignment.", "Kate")
task2 = Task("Prepare the project for class.", "James, Ann")

task3 = task1 + task2
print(task3.description)  # "Finish the assignment.\nPrepare the project for class."
print(task3.team)  # "Kate, James, Ann"