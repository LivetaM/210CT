import sys
sys.setrecursionlimit(8000) #increases recursion limit
def prime_Number(n, i):
    if n == i and n/1==n:
        return ("n is a prime number")
    elif (n%i)==0:
        return ("n is not a prime number")
    else:
        return (prime_Number(n, i+1))
        
   

print (prime_Number(1132, 2))
            
    
