
#chapter 2
#que 1
a=int(input("enter the num1="))
b=int(input("enter the num2="))
sum=a+b
print("sum of number =",sum)

#que 2
c=int(input("enter the num1="))
d=int(input("enter the num2="))
reminder=c%d
print("Reminder of number =",reminder)

#que 3
e=10
f="10"
type(e)
type(f)

#que 4
g=int(input("enter the num1="))
h=int(input("enter the num2="))
if (g>h):
 print("g is greater than h")
else :
 print("h is greater than g")

#que 5
i=int(input("enter the num1="))
j=int(input("enter the num2="))
average=(a+b)/2
print("average of two numbers=",average)

#que 6
n=int(input("enter the number="))
square=n*n
print("square of the number=",square)

#chapter 3
#que 1 
name=input("enter the name ")
print(f"GOOD AFTERNOON {name}")

#que 2
name=input("enter the name ")
date=input("enter the date ")
print(f'''letter = 
Dear {name},
You are selected!
{date}
''')
#another way to solve que 2
letter = '''Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>" , "HARRY").replace("<|Date|" ,"12 june 2026"))

#que 3 to find double space index
a = "I am  coding  in my  laptop"
print(a.find("  "))

#que 4
a = "I am  coding  in my  laptop"
print(a.replace("  "," "))
print(name) #strings are immutable which means that you cannot change them by running functions on them 

#que 5
letter = "Dear Harry,\n\t This python course is nice.\n Thanks!"
print(letter)

#chapter 4
#que 1 
marks = []

for i in range(7):
    marks.append(input("Enter fruit name: "))

print(marks)

#another way to solve que 1
fruit=[]
f1=input("enter Fruit name ")
fruit.append(f1)
f2=input("enter Fruit name ")
fruit.append(f2)
f3=input("enter Fruit name ")
fruit.append(f3)
f4=input("enter Fruit name ")
fruit.append(f4)
f5=input("enter Fruit name ")
fruit.append(f5)
f6=input("enter Fruit name ")
fruit.append(f6)
f7=input("enter Fruit name ")
fruit.append(f7)
print(fruit)

#que 2
marks = []

for i in range(7):
    marks.append(int(input("Enter mark name: ")))
marks.sort()
print(marks)

#que 3 
a = (223,343,"harry")
#a[2]="larry" it will show erorr

#que 4
l=[1,2,4,5]
print(sum(l))

#que 5
a = (7, 0, 8, 0, 0, 9)
n=a.count(0)
print(n)

#chapter 5
#que 1 
words={
   "madad":"help",
   "prem":"love",
   "tutna":"broken"
}
word=input("enter the word to know meaning : ")
print(words[word])

#que 2
s=set()
n=input("enter number:")
s.add(int(n))
n=input("enter number:")
s.add(int(n))
n=input("enter number:")
s.add(int(n))
n=input("enter number:")
s.add(int(n))
n=input("enter number:")
s.add(int(n))
n=input("enter number:")
s.add(int(n))
n=input("enter number:")
s.add(int(n))
n=input("enter number:")
s.add(int(n))
print(s)

#another method to solve que 2
numbers = []

for i in range(8):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Unique numbers are:", set(numbers))

#que 3 
s=set()
s.add(18)
s.add("18")

#que 4
r = set()
r.add(20)
r.add(20.0)
r.add('20')
print(len(r))

#que 5
s={}
print(type(s))

#que 6
d={}
name=input("enter friends name ")
language=input("enter friends language ")
d.update({name: language})
name=input("enter friends name ")
language=input("enter friends language ")
d.update({name: language})
name=input("enter friends name ")
language=input("enter friends language ")
d.update({name: language})
name=input("enter friends name ")
language=input("enter friends language ")
d.update({name: language})
print(d)

#que 7
d={}
name=input("enter friends name ")
language=input("enter friends language ")
d.update({name: language})
name=input("enter friends name ")
language=input("enter friends language ")
d.update({name: language})
name=input("enter friends name ")
language=input("enter friends language ")
d.update({name: language})
name=input("enter friends name ")
language=input("enter friends language ")
d.update({name: language})
print(d) #the key will choose second value if we enter same key twice in dictionary

#que 8
d={}
name=input("enter friends name ")
language=input("enter friends language ")
d.update({name: language})
name=input("enter friends name ")
language=input("enter friends language ")
d.update({name: language})
name=input("enter friends name ")
language=input("enter friends language ")
d.update({name: language})
name=input("enter friends name ")
language=input("enter friends language ")
d.update({name: language})
print(d)#there will be no change in dictionaryif the value is same but key is different in dictionary

#que 9
s = {8, 7, 12, "Harry", [1,2]}
s[4][0]=10 #we can't include list in set because list is mutable and we can't change the value of set but we can change the value of list which is included in set so it will show error


#chapter 6
#que 1 
a=int(input("enter the num1="))
b=int(input("enter the num2="))
c=int(input("enter the num3="))
d=int(input("enter the num4="))
if(a>b and a>c and a>d):
    print("a is greatest")
elif(b>a and b>c and b>d):
    print("b is greatest")
elif(c>a and c>b and c>d):
    print("c is greatest")
else:
    print("d is greatest")

#que 2
m1=int(input("enter the marks="))
m2=int(input("enter the marks="))
m3=int(input("enter the marks="))
percentage=(((m1+m2+m3)/300)*100)
print("percentage=",percentage)
if(percentage>=40 and m1>=33 and m2>=33 and m3>=33):
    print("student has passed ",percentage)
else:
    print("student has failed ",percentage)

#que 3
p1="Make a lot of money" 
p2="buy now" 
p3="subscribe this" 
p4="click this"
message=input("enter the message ")
if (message==p1 or message==p2 or message==p3 or message==p4):
    print("This is a spam message")
else:
    print("This is not a spam message")

#que 4
username=input("enter the username=")
count=len(username)
print(count)

#que 5
l=["Aman", "Anshul", "Anshika", "Anshul", "Anshika"]
name=input("enter the name=")
l.append(name)
if name in l:
    print("your name is in the list")
else:
    print("your name is not in the list")

#que 6
marks=int(input("enter the marks="))
if(marks<=100 and marks>=90):
    print("Ex grade")
elif(marks>=80 and marks<90):
    print("A grade")
elif(marks>=70 and marks<80):
    print("B grade")
elif(marks>=60 and marks<70):
    print("C grade")
elif(marks>=50 and marks<60):
    print("D grade")
else:
    print("F grade")
print("your grade is ",marks)

#que 7
post=input("enter the post ")
if ("harry".lower() in post.lower()):
    print("post is talking about harry")
else:
    print("post is not talking about harry")


#chapter 7
#que 1
number=int(input("enter the number="))
for i in range(1,11):
    print(f"{number} x {i} = {number*i}")

#que 2
l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if name.startswith("S"):
        print(f"hello {name}")

#que 3
number=int(input("enter the number="))
i=1
while (i<11):
    print(f"{number} x {i} = {number*i}")
    i+=1

#que 4
num=int(input("enter the number "))
for i in range(2,num):
    if num%i==0:
        print("number is not prime")
        break
else:
    print("number is prime")

#que 5
i=0
sum=0
n=int(input("enter the number="))
while i<n:
    sum+=i
    i+=1
print("sum of n natural number=",sum)

#que 6
i=0
factorial=1
n=int(input("enter the number="))
for i in range(1,n+1):
    factorial*=i
print("factorial of the number=",factorial)

#que 7
'''
for n=3
  *
 ***
*****
'''
n=int(input("enter the number "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("\n")

#que 8
'''
for n=3
  *
 **
 ***
'''
n=int(input("enter the number "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*i,end="")
    print("\n")

#que 9
'''
for n=3
***
**
***
'''
n=int(input("enter the number "))
for i in range(1,n+1):
    if i%2!=0:
        print("*"*n,end="")
        print("\n")
    else:
        print("*"*(n-1),end="")
        print("\n")

#que 10
number=int(input("enter the number="))
for i in range(1,11):
    print(f"{number} x {11-i} = {number*(11-i)}")


#chapter 8
#que 1
a=int(input("enter the num1="))
b=int(input("enter the num2="))
c=int(input("enter the num3="))
def is_greater(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
result = is_greater(a, b, c)
print(f"The greatest number is: {result}")

#que 2
celcius=int(input("enter the temperature in celcius="))
def celcius_to_fahrenheit(celcius):
    fahrenheit=(celcius*9/5)+32
    return fahrenheit
fahrenheit = celcius_to_fahrenheit(celcius)
print(f"Temperature in Fahrenheit: {fahrenheit}")

#que 3
print("a")
print("b")
print("c", end="")
print("d", end="") # To avoid new line after printing c and d we use end="" in print function

#que 4
n=int(input("enter the number="))
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

print(sum(n))

#que 5
n=int(input("enter the number "))
def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)
pattern(n)

#que 6
inches=int(input("enter the length in inches="))
def inches_to_centimeters(inches):
    centimeters=inches*2.54
    return centimeters
print(f"length in centimeters={inches_to_centimeters(inches)}")

#que 7
def rem(l,word):
    n=[]
    for item in l:
       if not(item==word):
           n.append(item.strip(word))
    return n
l=["Harry", "Soham", "Sachin", "Rahul"]
print(rem(l, "an"))

#que 8
number=int(input("enter the number="))
def multiply(n):
    for i in range(1,11):
        print(f"{number} x {i} = {number*i}")
multiply(number)

#chapter 9
#que 1
f=open("poem.txt")
content=f.read()
if "twinkle" in content:
    print("twinkle is present in the content")
else:
    print("twinkle is not present in the content")

#que 2
import random
def game():
    print("You are playing the game..")
    score=random.randint(1,62)
    #fetch the hiscore 
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if (hiscore==""):
           hiscore=int(hiscore)
        else:
             hiscore=0 
    print(f"Your score:{score}")
    if (score>=hiscore):
        #write this hiscore to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    return score

game()
