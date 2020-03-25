import numpy as np

Input = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
Intermediate = []
while len(Input) > 0:
    random_index = np.random.randint(0, len(Input))
    string = Input[random_index] 
    Intermediate.append(string)
    Input.pop(random_index)


Output = [[], [], [], [], []]
for i in range(25):
    if i % 5 == 0:
        Output[0].append(Intermediate[i])
    if i % 5 == 1:
        Output[1].append(Intermediate[i])
    if i % 5 == 2:
        Output[2].append(Intermediate[i])
    if i % 5 == 3:
        Output[3].append(Intermediate[i])
    if i % 5 == 4:
        Output[4].append(Intermediate[i])

print(Output)