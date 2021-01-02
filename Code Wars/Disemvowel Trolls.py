def disemvowel(string):
    vowelList = ['a','e','i','o','u', 'A','E','I','O','U']
    for vowel in vowelList:
        newString = string.replace(vowel,"")
        string = newString
    return newString
    

teste = "This website is for losers LOL!"
print(disemvowel(teste))