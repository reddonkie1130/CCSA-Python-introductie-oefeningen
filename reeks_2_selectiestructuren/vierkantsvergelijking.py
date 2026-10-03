a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4 * a *c  
res_POS = (-b + d**0.5) /(2 *a) 
res_NEG = (-b - d**0.5) / (2 *a)

if(d < 0):
    print("geen wortels")
elif(d > 0):
    print("twee wortels")
    print(res_POS)
    print(res_NEG)
    
else:
    print("een wortel")
    print(-b/2*a)


    