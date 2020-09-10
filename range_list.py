# number = list(range(1,11))
# print(number)                          # output = [1,....,10]

# print(number.pop())                    # output = 10

# number.pop()
# print(number)                          # output = [1,....9] 


# print(number.index(4))                 # output = 3

# NUMBER =  [1,2,3,4,1,2,3]
# print(NUMBER.index(1,2))                 # output = 4


# number = [1,2,3,4,5]
# def negative(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative

# print(negative(number))                  # output = [-1,-2,-3,-5]


# n = int(input("Enter your number : "))
# number = list(range(1,n+1))                # list range 
# def square(n):
#     num = []
#     for i in n:
#         num.append(i*i)
#     return num
# print(square(number))                      # output = 1^2 ,....,N=n^2


# n = int(input("Enter your last number : "))
# number = list(range(1,n+1))
# def reverse(r):
#     num = []
#     for i in range(len(r)):
#         popped = r.pop()
#         num.append(popped)
#     return num

# print(reverse(number))               #input = 2 // output = [2,1]


# name = ["apple" , "mango"]
# def reverse(r):
#     re = []
#     for i in r:
#         re.append(i[::-1])
#     return re

# print(reverse(name))


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



# n = int(input("Enter number , To stop press 0 : "))
# neg_count = 0
# pos_count = 0
# ne = []
# po = []
# while True: 
#     if n == 0:
#         break
#     else:
#         if n < 0:
#             ne.append(n)
#             print("negative")
#             n = int(input("Enter number : "))
#             neg_count += 1  
#         else:
#             po.append(n)
#             print("positive")
#             n = int(input("Enter number : "))
#             pos_count += 1  

# print("positive numbers :{}\nnegative numbers :{}".format(po,ne))
# print("number of positive numbers :{}\nnumber of negative numbers :{}".format(pos_count,neg_count))



  

    