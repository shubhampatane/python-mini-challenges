# --------------
#Code starts here
def palindrome(num):
    flag=1
    copy = num
    num =num+1
    if(flag==1):
        res = [int(x) for x in str(num)]
        ser = [int(x) for x in str(num)]
        ser.reverse()
        if(res==ser):
            return num
        else:
            return palindrome(num)



# --------------
#Code starts here
def a_scramble(str_1,str_2):
    x = str_1
    y = str_2
    x = x.lower()
    y = y.lower()
    a = [i for i in x]
    b = [i for i in y]
    flag = 1
    print(x,y)
    for i in b:
        if(i in a):
            a.remove(i)
        elif(i not in a):
            flag = 0
    if(flag==1):
        return True
    else:
        return False



# --------------
#Code starts here
def check_fib(num):
    li = []
    a=0
    b=1
    li.append(0)
    li.append(1)
    n=num
    while(n-2):
        c=a+b
        a=b
        b=c
        li.append(c)
        n=n-1
    if(num in li):
        return True
    else:
        return False




# --------------
#Code starts here
def compress(word):
    word = word.lower()
    at = []
    st = [x for x in word]
    i=1
    while (i<=len(st)-1):
        count = 1
        while(st[i-1]==st[i]):
            count=count + 1
            i = i+1
            if(i==len(st)):
                break
        at.append(st[i-1])
        at.append(count)
        i= i+1
    ans = ""
    if(st[len(st)-1]!=st[len(st)-2]):
            at.append(st[len(st)-1])
            at.append(1)
    for i in at:
        ans+=str(i)
    return ans


# --------------
#Code starts here
def k_distinct(string,k):
    at = []
    string = string.lower()
    res = [x for x in string]
    for i in range(0,len(res)):
        if(res[i] not in at):
            at.append(res[i])
    if (len(at)==k):
        return True
    else:
        return False
print(k_distinct("banana",4))


