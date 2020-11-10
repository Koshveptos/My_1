x = input()
a = []
count2 = 0
count = 0
if x.count('[') == x.count(']') and x.count('(') == x.count(')') and x.count('{') == x.count('}'):
    for i in x:
        if i == '(':
            a.append(')')
            count2 += 1
        elif i == '{':
            a.append('}')
            count2 += 1
        elif i == '[':
            a.append(']')
            count2 += 1
        elif i == a[-1]:
            del a[-1]
            count += 1
        else:
            continue
if count == count2 and count > 0:
    print('correct')
else:
    print('incorrect')
