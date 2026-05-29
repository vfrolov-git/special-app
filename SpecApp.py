# Test GIT
for i in range(2, 7):
    if i % 2 == 0:
        print(f'Even number{i}')
        continue
    print(f'Odd number {i}')

print('Lambda: ', list(map(lambda x: x + 3, [1, 2, 3])))  #final version

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for element in row:
        print(f' Matrix element {element}')


# Test remote branch
# Recursion on main special-app branch
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(f'Factorial = ', factorial(7)) # change n to test Github

# test origin + remote together
def future(): # blanc func
    pass
