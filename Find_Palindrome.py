/*

The program to find if the given number and the given string are palindromes

*/


def palindrome(n):
    temp = n
    rev = 0
    while temp!=0:
        rev = (rev*10)+(temp%10)
        temp = temp // 10

    if n==rev:
        print "Number is palindrome"
    else:
        print("Number is not a palindrome") 
        
 def string_pal(s):
    s = s.replace(' ','')
    s = s.lower()
    if s[::] == s[::-1]:
        print "The string is palindrome"
    else:
        print "The string is not palindrome"
 

n = input(int("Enter the number:"))
palindrome(n)

s = input("Enter a word:")
string_pal(s)
