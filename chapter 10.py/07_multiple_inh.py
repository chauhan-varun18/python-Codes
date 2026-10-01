class A:

    varA = "wlcm to cls A"

class B:

    varB = "wlcm to cls b"

class C(A,B):

    varC = "wlcm to cls A or B"

c1 = C()  # c k nya obj.

print(c1.varA)
print(c1.varC)