"""a=input()
b=[]
k=1
for i in a:
    if i=='(' or i=='[' or i=='{':
        b.append(i)
    elif i==')' or i==']' or i=='}':
        if i==')' and b[-1]=='(':
            b.pop()
        elif i==']' and b[-1]=='[':
            b.pop()
        elif i=='}' and b[-1]=='{':
            b.pop()
        else:
            k=10
if k==10:
    print("no")
else:
    print("yes")


stack=[]
s=input()
n=len(s)
flag=1
if s[0]==']' or s[0]=='}' or s[0]==')':
    print(False)
else:
    for i in range(n):
        if s[i]=='[' or s[i]=='(' or s[i]=='{':
            stack.append(s[i])
        elif s[i]==']' or s[i]=='}' or s[i]==')':
            if (stack[-1]=='{' and s[i]=='}') or (stack[-1]=='[' and s[i]==']') or (stack[-1]=='(' and s[i]==')'):
                stack.pop()
            else:
                flag=0
                break
        else:
            flag=-1
            break
    if flag==1:
        print(True)
    elif flag==0:
        print(False)
    else:
        print("Invalid paranthesis")"""


while True:
    a = input()
    if len(a)%2==1:
        print('no')
        continue
    b = []
    k = 1
    if a[0]==')' or a[0]=='}' or a[0]==']':
        print('no')
        continue
    for i in a:
        if i == '(' or i == '[' or i == '{':
            b.append(i)
        elif i == ')' or i == ']' or i == '}' and not len(b)==0:
            if i == ')' and b[-1] == '(' and not len(b)==0:
                b.pop()
            elif i == ']' and b[-1] == '[' and not len(b)==0:
                b.pop()
            elif i == '}' and b[-1] == '{' and not len(b)==0:
                b.pop()
            else:
                k = 10
    if k == 10:
        print('no')
    else:
        print('yes')





