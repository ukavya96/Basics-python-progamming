def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count    
string=input("enter the vowels")

v=count_vowels(string) 
print(v)   