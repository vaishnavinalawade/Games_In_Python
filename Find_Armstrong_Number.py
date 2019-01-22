/*
* problem description : program to find if the given number is an armstrong number
*/

n = int(input("Enter the number:"))
t = n
s = 0
while t>0:
    r = t%10
    s += r**3
    t //= 10

if n == s:
    print "{x} is an Armstrong number".format(x = n)
