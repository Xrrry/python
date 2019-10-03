#filter
list_x = [1,2,3,4,1,1,3,3,9,6,7,5,4]

r = filter(lambda x:True if x<6 else False,list_x)
print(list(r))