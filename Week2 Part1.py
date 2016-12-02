def hpersquare(n):
    i = 0
    parameter = 4*n
    new = list()
    while i in range(n):
        i=i+1 
        perfectsquare = i*i
        if perfectsquare <= parameter:
            new.append(perfectsquare)
    return (max(new)) 
        
    
print (hpersquare(15))
