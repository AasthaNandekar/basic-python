a = 31
t = type(a) #class <int>
print(t)
b = 31.4
t= type (b) #class<float>
print(t)
c = "10.22"
t = type (c) #class<str>#agar kisiko 
print(t)
d="40.1"
e=float(d) #d but type should be float
t=type(e)
print(t)

# Input() function

a = input ("Enter number 1:")
b = input ("Enter number 2:")

print("Number a is:",a)
print("Number b is:",b)
print("Sum:",a+b) #result will always in string only

a =int(input ("Enter number 1:"))
b = int(input ("Enter number 2:"))

print("Number a is:",a)
print("Number b is:",b)
print("Sum:",a+b) 