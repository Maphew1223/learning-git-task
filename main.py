list1 = ['chleb', 'bułki', 'pączek']
list2 = ['marchew', 'seler', 'rukola']
dict1 = {'piekarnia': list1, 'warzywniak': list2}
print("Lista zakupów")

for i , v in dict1.items():
    print("Idę do", i.capitalize(), "i kupuję", v)
print("W sumie kupuję", (list1.__len__()+list2.__len__()), "produktów")