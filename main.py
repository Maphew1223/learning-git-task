list1 = ['chleb', 'bułki', 'pączek']
list2 = ['marchew', 'seler', 'rukola']
dict1 = {'piekarnia': list1, 'warzywniak': list2}
print("Lista zakupów")

for i , v in dict1.items():
    print("Idę do", i.capitalize(), "i kupuję", v)
print("W sumie kupuję", (list1.__len__()+list2.__len__()), "produktów")


for x in range(101):
    if x % 3 == 0:
        print(x)
print()

j = 0
while True:
    if j % 3 == 0:
        print(j)
    else:
        pass
    j += 1
    if j >100:
        
        break