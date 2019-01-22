/*
* problem description : program to find the factorial values of numbers for some given number of input
*/


num = input(int("Enter a number:"))
fac = 1
i = 1
l = []
while i <=num:
    fac = fac * i
    i = i + 1
    l.append(fac)
print("The Factorial for %s :" %(num))
print(l)
