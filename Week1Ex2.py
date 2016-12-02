def find_Factorial(n):
    if n==0:
        return (1)
    else:
        factorial = n*find_Factorial(n-1) #recursively finds factorial
        return(factorial)

def reverse_Factorial(n):
    f = find_Factorial(n)
    string = str(f)
    return (''.join(reversed(string))) #reverses string, that contains factorial

def trailing_Zeros(n):
    reversed_String = reverse_Factorial(n)
    count = 0
    number = '123456789'
    for i in reversed_String:
        if i == '0':#counts first string 0's 
            count = count + 1
        elif i in number:#stops going through the reversed_String if i!=0
            break
    return count
        
print (trailing_Zeros(10))
