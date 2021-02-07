s=input()
result=0
array=[]
for i in s:
    if i>='0' and i<='9':
        result+=int(i)
    else:
        array.append(i)
array.sort()
array.append(str(result))

print(''.join(array))