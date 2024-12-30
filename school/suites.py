a = 2
u = a
n = float(a)

for n in range (20):
    n = n+1
    u = 0.5 * (u+a/u)
print (u, sqrt(a))