
name = [1,3,4,6]
neg = []
for i in name:
    neg.append(-i)

print(neg)                 # general method // output = [-1, -3, -4, -6] 

new = [-i for i in name]
print(new)                          # output = [-1, -3, -4, -6]// list comprehension 


name = ['shuvranil','nil']
nam = []
for cahr in name:
    nam.append(cahr[::-1])
print(nam)                                         # general method // output =['linarvuhs', 'lin']


name = ['shuvranil','nil']
new = [char[::-1] for char in name]
print(new)                                         # output = ['linarvuhs', 'lin']// list comprehension 



odd = [i for i in range(1,11) if i%2==0]
even = [i for i in range(1,11) if i%2!=0]
print(even)                                          # [2, 4, 6, 8, 10]
print(odd)                                           # output = [1, 3, 5, 7, 9]


lis = [2,3,4,1.2,'nil',['s','f']]
num = []
for i in lis:
    if (type(i)==int or type(i)==float):
        num.append(str(i))

print((num))                                         # output = ['2', '3', '4', '1.2']// normal method 


__________________________________________________
lis = [2,3,4,1.2,'nil',['s','f']]
def string(l):
    return [str(i) for i in l if (type(i)==int or type(i)==float)]
print(string(lis))                                                    # output = ['2', '3', '4', '1.2'] // list comprehension method 

num = [[i for i in range(1,3)]  for j in range(3)]
print(num)



