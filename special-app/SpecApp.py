# Test GIT
for i in range (2, 20):
    if i % 2 == 0:
        print(f'Even number{i}')
        continue
    print(f'Off number {i}')

print('Lambda', list(map(lambda x: x + 1, [1, 2, 3])))