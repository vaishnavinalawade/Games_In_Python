/*

The program to find the given number is a palindrome

*/


n = input("Enter the number:")

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
 
 palindrome(n)
