# 9.9. ジェネレータ (generator) =========================
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        # 何らかのデータを返すときには yield 文を使います
        yield data[index] 

for char in reverse('golf'):
    print(char)

'''
f
l
o
g
'''

# 9.10. ジェネレータ式  =========================

# sum of squares
sum(i*i for i in range(10)) # 285


xvec = [10, 20, 30]
yvec = [7, 5, 3]
# dot product
sum(x*y for x,y in zip(xvec, yvec)) # 260


unique_words = set(word for line in page  for word in line.split())

valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
# ['f', 'l', 'o', 'g']
