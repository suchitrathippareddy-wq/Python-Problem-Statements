#Check positive/negative
def negative_positive(a):
    for i in a:
        if i < 0:
            print(i,'is negative')
        else:
            print(i,'is negaive')

a=list(map(int,input("enter values:").split()))
negative_positive(a)