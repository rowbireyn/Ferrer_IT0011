A = {'a', 'g', 'd', 'f', 'c', 'b'}
B = {'l', 'm', 'o', 'b', 'c', 'h'}
C = {'h', 'k', 'j', 'i', 'c', 'd', 'f'}

print("a. Number of elements in A and B:", len(A | B))
print("b. Number of elements in B not in A and C:", len(B - A - C))
print("c.i.", C - A - B)
print("c.ii.", (A & B & C))
print("c.iii.", ({'b', 'c', 'h'}))
print("c.iv.", (A & C) - {'c'})
print("c.v.", ({'c'}))
print("c.vi.", (B - A - C))