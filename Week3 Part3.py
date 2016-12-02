def vowels_Remove(s):
    vowels = "aeiouAEIOU"
    if len(s)<1: 
        return (s)
    elif s[0] in vowels: 
        return (vowels_Remove(s[1:]))
    return (s[0] + vowels_Remove(s[1:]))
            

        
print (vowels_Remove("beautiful"))

