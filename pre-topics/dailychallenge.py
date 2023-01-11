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

# 2023.1.9 print all winner
rounds_input = int(input())
result_list = []
for i in range(rounds_input):
    result_list.append(input())

ans = {}
for result in result_list:
    temp = result.split(' ')
    if temp[0] in ans:
        if temp[1] == 'win':
            ans[temp[0]] += 1

    else:
        if temp[1] == 'win':
            ans[temp[0]] = 1
        else:
            ans[temp[0]] = 0

for key in ans:
    if ans[key] > 0:
        print([key] * ans[key])
        print(ans[key])