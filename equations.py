def exponent (x):
    result =1 
    i=1
    mone=1
    mechane=1
    while ( i<=170):
        mone=mone*x
        mechane=mechane*i
        result+= mone/mechane
        i+=1
    return result

def Ln(x):
    y_n=x-1.0
    y_n1= y_n + 2 * (x-exponent(y_n))/(x+exponent(y_n))
    while( abss(y_n-y_n1)>0.001):
        y_n=y_n1
        y_n1= y_n + 2 * (x-exponent(y_n))/(x+exponent(y_n))
    return(y_n1)

def abss(x):
    if(x>=0):
        return x
    return -x

def XtimesY(x,y):
    if(x>=0):
        return  float('%0.6f' % exponent(y*Ln(x)))
    return 0.0
def sqrt(x,y):
    return XtimesY(y,1/x)

def calculate(x):
    answer= exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
    return answer
    
x= input("enter a x:")
try: 
    x= float(x)
    print(calculate(x)) 
except:
    x=0.0
    print(x)

   

#print(XtimesY(x,y))
#print(sqrt(x, y)) 






  

