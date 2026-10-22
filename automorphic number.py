a=int(input('givd:'))

b=a
d=1
c=a**a
while a>0:
    d=d*10
    a=a//10
if c % d == b:
    print(f"{b} is an automorphic number number" )
else:
    print(f"{b} is not an automorphic number")
    """
a = int(input("Give: "))

b = a
c = a * a
d = 1

while a > 0:
    d = d * 10
    a = a // 10

if c % d == b:
    print(f"{b} is an automorphic number")
else:
    print(f"{b} is not an automorphic number")"""