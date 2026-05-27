# Test GIT
for i in range (2, 7):
    if i % 2 == 0:
        print(f'Even number{i}')
        continue
    print(f'Odd number {i}')

print('Lambda: ', list(map(lambda x: x + 5, [3, 4, 5])))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for element in row:
        print(f' Matrix element {element}')
