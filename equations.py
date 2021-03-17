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
    if(x<=0):
        return 0.0
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
    if(x>0.0):
        return  float('%0.6f' % exponent(y*Ln(x)))
    return 0.0
def sqrt(x,y):
    if (y<0 or x==0):
        return 0.0   
    return XtimesY(y,1/x)

def calculate(x):
    answer= exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
    return answer
  

                      


  

