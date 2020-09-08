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

