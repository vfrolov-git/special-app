# Test GIT
for i in range (2, 7):
    if i % 2 == 0:
        print(f'Even number{i}')
        continue
    print(f'Odd number {i}')



print('Lambda: ', list(map(lambda x: x + 3, [1, 2, 3]))) #final version


matrix = [[1, 2], [4, 5]]

for row in matrix:
    for element in row:
        print(f' Matrix element {element}')


# New branch catalog-filter
def count():
    pass
