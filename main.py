"""
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

tea_recipe = ["włącz czajnik", "znajdź opakowanie herbaty", "zalej herbatę", "nalej wody do czajnika", "wyjmij kubek", "włóż herbatę do kubka"]
print(tea_recipe)
print()
tea_recipe_sorted = [tea_recipe[3], tea_recipe[0], tea_recipe[4], tea_recipe[1], tea_recipe[5], tea_recipe[2]]
print(tea_recipe_sorted)
"""
print("special greetings")