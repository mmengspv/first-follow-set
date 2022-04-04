# Contributor
# 1.สุภเวช อมรรักษากุล 6210406734
# 2.แพรว ปักษานนท์   6210406645

import re


def first(pd):
    count = 0
    pd_split = pd.split("=")
    nonterminal = pd_split[0]
    first_data = pd_split[1][0]
    if first_data.islower():
        if first_data not in first_set[nonterminal]:
            first_set[nonterminal].append(first_data)
            count += 1
    else:
        if first_data in first_set:
            for i in first_set[first_data]:
                if i not in first_set[nonterminal]:
                    first_set[nonterminal].append(i)
                    count += 1
        else:
            if first_data not in first_set[nonterminal]:
                first_set[nonterminal].append(first_data)
                count += 1
    return count


num_production = int(input("Enter number of production: "))

production = []
first_set = {}

for i in range(num_production):
    production_input = input("Enter production :")
    production.append(production_input)
    production_input = production_input.split("=")
    non_terminal = production_input[0]
    if non_terminal not in first_set:
        first_set[non_terminal] = []
    for i in production_input[1]:
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:Є]')
        if (i.islower() or regex.search(i) != None) and i not in first_set:
            first_set[i] = [i]


count = 1
while(True):
    if count == 0:
        break
    count = 0
    for i in production:
        count += first(i)

print()
print("----------------------- First Set -------------------------")
print()

for x, y in first_set.items():
    print("%s = %s" % (x, y))
