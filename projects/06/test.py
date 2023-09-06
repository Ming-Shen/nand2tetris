line = ['//abcde','\n','fgh']
print(line[0][0:2])
for str in line:
    for i in range(len(str)):
        if str[i] == '\n':
                break
        elif str[i:2] == '//':
            break
        elif str[i] == ' ':
            continue
        else:
            print(str[])
    i = 0
