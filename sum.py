def sum(n): 
    sm=0
    for i in range(0, n):
               
                sm+=(((2*i)+1)**2)/(((2*i)+1)**3)
    return sm
                
q=input()
n=int(q)
print(sum(n))
