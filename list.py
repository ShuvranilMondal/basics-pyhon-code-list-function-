num = [1,2,3,4,5]
print("number is {} ".format(num))

words = ["apple", "mango" , "strawberry" , "goava"]
print("{}".format(words[2]))
print("{}".format(words[-1]))
words[1] = "nil"                              #add variable in list//
print(words)

menu = []
name = input("Enter : ")
menu.append(name)
print(menu)

words = ["apple", "mango" , "strawberry" , "goava"]
# words.insert(2 , "nil")
words[2] = "nill"
print(words)


words = ["apple", "mango"]
words.pop()
print(words)

name= input("Enter your fruit : ")
nam = name.lower().strip()
words = ["apple", "mango" , "strawberry" , "goava" , "apple"]
if nam  in words:
    print("{} is present".format(nam))
else:
    print("{} is not present".format(nam))

count = words.count(nam)
print("{} available".format(count))


number = [1,3,2,7,4]
number.sort()
print(F"{number}")

matrix = [[1,2,3],[4,5,6],[6,7,8]]
print(matrix[2])                        # output = [6,7,8]

for i in matrix:
    print(i)                            # use for loop

for sub in matrix:
    for i in sub:
        print(i)                        # output = 1,2,3......8 // use to find sub elements of a matrix 


n = int(input("Enter : "))
sub = matrix[n]
for i in sub:
    print(i)                             # input = 0 // output = 1,2,3 //

print(matrix[1][0])                        # output = 4 // sub matrix element find 
