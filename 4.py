### 4.1. if Statements ========

x = int(input("Please enter an integer: "))
    # Please enter an integer: 42
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
    # More

### 4.2. for Statements ========

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
    # cat 3
    # window 6
    # defenestrate 12

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)
# {'Hans': 'active', '景太郎': 'active'}

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)
# {'Hans': 'active', '景太郎': 'active'}

## 4.3. The range() Function ========

for i in range(5):
    print(i)

'''
0
1
2
3
4
'''

print(list(range(5, 10)))
# [5, 6, 7, 8, 9]

print(list(range(0, 10, 3))) # +30 step
# [0, 3, 6, 9]

print(list(range(-10, -100, -30))) # -30 step
# [-10, -40, -70]

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i + 1, a[i])
    
'''
1 Mary
2 had
3 a
4 little
5 lamb
'''

print(range(10)) # range(0, 10)

sum = sum(range(4)) # 0 + 1 + 2 + 3
print(sum) #6