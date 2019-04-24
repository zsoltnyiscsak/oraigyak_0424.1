A = {3,5,7,'a','c','string',3.14}
B = set(range(1,11))
C = set("almafa")

print(A)
print(B)
print(C)

D = A & B
E = A | B
print(D)
print(E)

F = A ^ B
print(F)
G = A-B
print(G)