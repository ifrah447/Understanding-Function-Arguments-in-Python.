# function is used to seperate the code and repeatbility is high
# there are four kind of arguments
# 1 DEFAULT ARGUMENT we can say that we can give default value while defining a function and if we will not give any value while calling the function then it will take the default value
def average(a=9,b=1):
  print("The average is ", (a + b) / 2)
average()
average(2)
average(2,3)
average(b=4)
# 2 KEYWORD ARGUMENT we can say that we can give value while calling the function while order is not matter but assign values to the correct parameter
average(b=4,a=2)
def avg(a,b,c=2):
  avg=(a+b+c)/3
  print(avg)
avg(2,3)
# 3 VARIABLE LENGTH ARGUMENT we
def averg(*numbers):
  sum=0
  for i in numbers:
    sum= sum + i
  print("average is: ",sum/len(numbers))
averg(2,3,4,5,6,7)
# arbitary argument are used to take input from user in the form of dic,list,tuple,set
def name(**name):
  print("hello",name["fname"],name["mname"],name["lname"])
name(fname="ifrah",mname="asghar ali",lname="khan")
name(fname="alveera",mname="sami",lname="sami")
name(fname="rida",mname="maheen",lname="jabeen")
# return statement is used to return the value of the expression back to the calling function
def average(a,b):
  return (a+b)/2  #return mtlb wapis chly jao is value ko ko lekey
  return 7 #jb do return ek he unit main ho toh phly wala mana jata
c=average(2,3)
print(c)

