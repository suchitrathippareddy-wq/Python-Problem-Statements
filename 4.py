#Check even or odd
def even_odd(a):
    for i in a:
        if i  % 2==0:
            print(i,"is even")
        else:
            print(i,"is odd")
a=list(map(int,input("enter values:").split()))
even_odd(a)