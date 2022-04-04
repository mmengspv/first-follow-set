# Contributor
# 1.สุภเวช อมรรักษากุล 6210406734
# 2.แพรว ปักษานนท์   6210406645

import re

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:Є]')


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


def follow(pd):
    count = 0
    pd_split = pd.split("=")
    nonterminal = pd_split[0]
    data = pd_split[1]
    for i in range(len(data)):
        if data[i].isupper() and regex.search(data[i]) == None:
            if i == len(data)-1:
                for j in follow_set[nonterminal]:
                    if j not in follow_set[data[i]]:
                        follow_set[data[i]].append(j)
                        count += 1
            elif data[i+1].isupper() and regex.search(data[i+1]) == None:
                for j in first_set[data[i+1]]:
                    if j not in follow_set[data[i]] and j != "Є":
                        follow_set[data[i]].append(j)
                        count += 1
                if "Є" in first_set[data[i+1]]:
                    for j in follow_set[data[i+1]]:
                        if j not in follow_set[data[i]]:
                            follow_set[data[i]].append(j)
                            count += 1
            elif data[i+1].islower() or regex.search(data[i+1]) != None:
                if data[i+1] not in follow_set[data[i]]:
                    follow_set[data[i]].append(data[i+1])
                    count += 1

    return count


num_production = int(input("Enter number of production: "))

production = []
first_set = {}
follow_set = {}

for i in range(num_production):
    production_input = input("Enter production :")
    production.append(production_input)
    production_input = production_input.split("=")
    non_terminal = production_input[0]
    if non_terminal not in first_set:
        first_set[non_terminal] = []
    for i in production_input[1]:
        if (i.islower() or regex.search(i) != None) and i not in first_set:
            first_set[i] = [i]


count = 1
while(True):
    if count == 0:
        break
    count = 0
    for i in production:
        count += first(i)


for index, key in enumerate(production):
    non_terminal = key.split("=")[0]
    if index == 0:
        follow_set[non_terminal] = ["$"]
    else:
        if non_terminal not in follow_set:
            follow_set[non_terminal] = []


count = 1
while(True):
    if count == 0:
        break
    count = 0
    print("doloop")
    for i in production:
        count += follow(i)
    print(count)
    # break

print()
print("----------------------- First Set -------------------------")
print()

for x, y in first_set.items():
    print("%s = %s" % (x, y))

print()
print("----------------------- Follow Set -------------------------")
print()

for x, y in follow_set.items():
    print("%s = %s" % (x, y))
