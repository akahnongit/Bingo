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
    for j in range(5):
        if i % 5 == j:
            Output[j].append(Intermediate[i])

print(Output)