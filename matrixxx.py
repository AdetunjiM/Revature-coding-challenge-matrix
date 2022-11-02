
def id_matrix(m):
    outer=[]
    if m < 0:
        pos= -1*m
        for x in range(pos):
            inner=[]
            for y in range(pos):
                if pos-x-1 == y :
                    inner.append(1)
                else:
                    inner.append(0) 
            outer.append(inner)
            
        return(outer)
        
    else: 
        for x in range(m):
            inner=[]
            for y in range(m):
                if x == y :
                    inner.append(1)
                else:
                    inner.append(0) 
            outer.append(inner)
        return(outer)


m = int(input("Enter The input Value "))
result1 = id_matrix(m)
for x in result1:
    print(x) 
    
"""result1 = id_matrix(-3)
for x in result1:
    print(x)
print("### Positive Test###")
result2 = id_matrix(3)
for x in result2:
    print(x)"""