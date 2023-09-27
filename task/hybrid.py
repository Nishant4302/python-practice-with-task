class A:
    def dispay(self):
        print("A : I am ", self)

class B(A):
    # def dispay(self):
    #     print("B : I am ", self)
    pass
class C(A):
    # def dispay(self):
    #     print("C : I am ", self)
    pass
class D(B,A):
    # def dispay(self):
    #     print("D : I am ", self)
    pass
class G(D):
    # def dispay(self):
    #     print("G : I am ", self)
    pass
class F(C,D):
    # def dispay(self):
    #     print("F : I am ", self)
    pass
class H(F):
    # def dispay(self):
    #     print("H : I am ", self)
    pass

g = G()
print(g.dispay())


for  i in G.__mro__:
    print(i)

f = H()
print(f.dispay())


for  i in H.__mro__:
    print(i)