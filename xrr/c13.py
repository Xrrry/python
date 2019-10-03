#map/lambda
list_x = [1,2,3,4,5,6,7]

def sq(x):
    return x*x

f = map(sq,list_x)
print(list(f))
ff = map(lambda x:x*x,list_x)
print(list(ff))