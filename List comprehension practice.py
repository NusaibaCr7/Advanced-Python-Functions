num = int(input("Enter a number: "))

l1 = []
for i in range(0,num+1):
    l1.append(i)
    
print(l1)

odd = [i for i in l1 if i%2!=0]

print(odd)

fruits = ["apple", "orange", "banana","grapes","strawberry"]

capFruits = [fruit.capitalize() for fruit in fruits]

print(capFruits)