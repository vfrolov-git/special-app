# test file for git
print('folder spec-app-2, file test_git') # testing merge

n = 10
<<<<<<< HEAD
print(n)
for i in range(n):
    n -= 1

    print(n)


lmb = lambda a, b, c: a + b + c

# a,b,c = 1 ,2, 3
print(lmb(1, 2, 3))
=======

print('Number', n)

for i in range(n):
    n -= 1
    print(n)

>>>>>>> new-contacts
