d={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',50:'L',100:'C',500:'D',1000:'M',5000:'G',10000:'H'}
def roman(n,div):
    if(div>=10000 and n!=1):
        return n*d[10000]
    if(n<=3):
        return n*d[div]
    elif(n==4):
        return d[div]+d[5*div]
    elif(n>=5 and n<=8):
        return d[div*5]+(d[div]*(n-5))
    elif(n==9):
        return d[div]+d[div*10]
n=int(input())
div=1
s=''
while(n):
    l=int(n%10)
    if(l!=0):
        s=roman(l,div)+s
    div*=10
    n=n//10
print(s)