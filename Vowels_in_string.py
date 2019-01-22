/*
* problem description : program to find the number of time each vowel appears in a given string
*/

string = "I am a coder. I am very intelligent. I have lot of money. You are pretty. Oh! Eat Me Umbrella."
counts = {i:0 for i in 'aeiouAEIOU'}
for char in string:
    if char in counts:
        counts[char] += 1
for k,v in counts.items():
    print(k, v)
