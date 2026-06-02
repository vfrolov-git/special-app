# Test GIT
print('Add changes from new-contacts branch')

print('folder spec-app') # test merge
for i in range (2, 7):
    if i % 2 == 0:
        print(f'Even number{i}')
        continue
    print(f'Odd number {i}')


print('Lambda: ', list(map(lambda x: x + 3, [1, 2, 3]))) #final version


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for element in row:
        print(f' Matrix element {element}')
