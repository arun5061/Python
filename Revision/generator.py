x=[y*y for y in range(50)]
print(x)
z=(y*y for y in range(50))
for num in z:
    print(num)

def Sqrt(list):
    for i in list:
        yield(i*i)
print()
l=Sqrt(range(50))

for num in l:
    print(num)
