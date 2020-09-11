number = list(range(1,11))
print(number)                          # output = [1,....,10]

print(number.pop())                    # output = 10

number.pop()
print(number)                          # output = [1,....9] 


print(number.index(4))                 # output = 3

NUMBER =  [1,2,3,4,1,2,3]
print(NUMBER.index(1,2))                 # output = 4


number = [1,2,3,4,5]
def negative(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative(number))                  # output = [-1,-2,-3,-5]


n = int(input("Enter your number : "))
number = list(range(1,n+1))                # list range 
def square(n):
    num = []
    for i in n:
        num.append(i*i)
    return num
print(square(number))                      # output = 1^2 ,....,N=n^2


n = int(input("Enter your last number : "))
number = list(range(1,n+1))
def reverse(r):
    num = []
    for i in range(len(r)):
        popped = r.pop()
        num.append(popped)
    return num

print(reverse(number))               #input = 2 // output = [2,1]


name = ["apple" , "mango"]
def reverse(r):
    re = []
    for i in r:
        re.append(i[::-1])
    return re

print(reverse(name))


n = int(input("Enter your range : "))
number = list(range(1,n+1))

def odd_even(oe):
    odd  = []
    even = []
    for i in oe:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return  (F"number of odd numbers : {len(odd)} : {odd}\nnumber of even numbers : {len(even)} : {even}")
    r 
print(odd_even(number))         # output = [[odd numbers],[even numbers]]



n = int(input("Enter number , To stop press 0 : "))
neg_count = 0
pos_count = 0
ne = []
po = []
while True: 
    if n == 0:
        break
    else:
        if n < 0:
            ne.append(n)
            print("negative")
            n = int(input("Enter number : "))
            neg_count += 1  
        else:
            po.append(n)
            print("positive")
            n = int(input("Enter number : "))
            pos_count += 1  

print("positive numbers :{}\nnegative numbers :{}".format(po,ne))
print("number of positive numbers :{}\nnumber of negative numbers :{}".format(pos_count,neg_count))

number = int(input("Enter number : TO stop enter = 0 : "))
total_odd = 0
total_even =0
odd = []
even =[]
while True:
    if number == 0:
        break
    else:
        if number % 2 == 0:
            even.append(number)
            print("number is even")
            number = int(input("Enter number : TO stop enter = 0 :"))
            total_even += 1
        else:
            odd.append(number)
            print("number is odd")
            number = int(input("Enter number : TO stop enter = 0 :"))
            total_odd += 1

print(f"odd numbers :{odd} : number of odd :{total_odd}\neven numbers : {even} : number of even :{total_even}") 
            

number_1 = [1,3,4]
number_2 = [2,3,1]

def filter_num(n,l):
    output = []
    for i in n:
        if i in l:
            output.append(i)
    return output

print(filter_num(number_1,number_2))          # output = [1,3]


number = [20,4,1]

def cal_num(l):
    return max(l) - min(l)

print(cal_num(number))                    #  output = 19


name = [1,3,1,[2,3,2],[3,3]]

def find(l):
    total = 0
    for i in l:
        if type(i) == list:
            total += 1
    return total

print(find(name))                   # output = 2

  

    
