Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# An integer assignment 
age = 45
  
# A floating point 
salary = 1456.8
  
# A string 
name = "John"
dir(name)
  
print(age) 
print(salary) 
print(name)
print("Before declare: ", age) 

>>> name = "Info"
>>> print(name)
Info
>>> for i in range(3):
    print(name)
>>> for q in range(0,5):
    print(q)

    
def function1():

  print("Hello from the other side")

count = 0
while (count < 3):    
    count = count+1
    print(name)


count = 0
while (count < 3):    
    count = count+1
    print("Hello Geek")


l = ["one", "two", "three"]
for i in l:
    print(i)
     

t = ("one", "two", "three")
for i in t:
    print(i)
     
     
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s %d" %(i, d[i]))



letter = l

for letter in 'michael':
    pass
print('Last Letter :', letter)

for letter in 'michael':
 
    if letter == 'e' or letter == 'h':
        break
print('Current Letter :', letter)

box = ["one", "two", "three"]
for x in box:
  print(x)

new_box = ["one", "two", "three"]
for x in new_box:
  if x == "two":
    break
  print(x)


list_of_listss = [ 
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9] 
] 
  
print(list_of_listss) 

list_of_lists = [] 
  
 
list_of_lists.append([1, 2, 3]) 
list_of_lists.append([4, 5, 6]) 
list_of_lists.append([7, 8, 9]) 
  
print(list_of_lists)



plist = [1,2,3,4]
print(plist)

newlist = ["mike","kenny","ay","dawn"]
newlist.sort()
#descending order# thislist.sort(reverse = True)
print(newlist)
