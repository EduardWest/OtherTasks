x1=[1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1]
x2=[1,1,1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1]
x3=[-1,-1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,-1]
x=[x1,x2,x3]
x4=[1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1]
def weight(x):
    w=[]
    for i in range(len(x[0])):
        w.append([])
        for j in range(len(x[0])):
            w[i].append(0)
    for i in range(len(x[0])):
        for j in range(len(x[0])):
            w[i][j]=0
            if i!=j:
                for k in range(len(x)):
                    w[i][j]=w[i][j]+x[k][i]*x[k][j]
    return w

def hemming(a,b):
    if len(a)==len(b):
        k=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                k=k+1
        return k
    else:
        print('Неверно введены данные')

def vektor(a):    
    w=weight(x)
    s=[]
    n=0
    for i in range(len(a)):
        s.append(0)
    while hemming(a,s)!=0:
        if n!=0:
            a=s
        for i in range(len(w)):
            s[i]=0
            for j in range(len(w)):
                s[i]=s[i]+w[i][j]*a[j]
            if s[i]>=0:
                s[i]=1
            else:
                s[i]=-1
        n=n+1
    return s

def nero(a,x):
    d=[]
    for i in range(len(x)):
        d.append(hemming(a,x[i]))
    print(d.index(min(d))+1)
print(len(x))   
