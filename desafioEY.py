def jumpOnClouds(c):
    n=len(c)-1
    jumps= 0
    i=0 
    if n < 2 or n > 100:
        return "Type a list with more than 2 and less than 100 items"
    elif c[0] != 0 or c[-1] != 0:
        return "The first and the last item must be a 0"
    else:
        while i < n and (c[i] == 0 or c[i] == 1):
            if i<n-1 and c[i+2] == 0:
                i += 2
                jumps +=1
# Si al moverse dos lugares, cae sobre un globo verde, suma un salto
            elif c[i+1] == 0:
                i += 1
                jumps +=1
#Si al moverse un lugar cae sobre un globo verde, suma un salto 
            else: return "The list must only contain 1 and 0"    
    return jumps  

print(jumpOnClouds([0,0,1,0,1,0]))

