#dictionary
yicheng={"David":23,"Mary":22,"Gary":11}
print(yicheng["David"])

yicheng["yicheng"]=8
yicheng["yicheng2"]=16

print(yicheng)

print(3 in yicheng)
print("David" in yicheng)
print("yicheng3" not in yicheng)

print(yicheng.get("David"))
print(yicheng.get("yicheng3"))

#tuple
words=("yicheng","happy","sexy")#This is a tuple
print(words[0])

emptyTuple=()#This is empty tuple

#list
list=[1,2,3,4,5,6,7,8]
print(list[0:3])#print two numbers
print(list[3:5])

print(list[:5])#before fifth number 
print(list[5:])#after fifth number and included the fifth number

step=[1,2,3,4,5,6,7,8,9,9]
print(step[0:9:2])#from 0 to 9 , eg 1+2=3 3+2=5
print(step[::3])#print every value with 3
print(step[1::3])#from 1 print every 3 step
print(step[1:-1])#count from 1 from last 1

#list comprehension
cube=[i**3 for i in range(20)]
print(cube)

cube1=[i**2 for i in range(20) if
      i**2%2==0]
print(cube1)

print("{0}{1}{0}".format("yicheng","handsome"))
