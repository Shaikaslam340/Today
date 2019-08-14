import time
a=time.asctime()
b=a[0:3]
if(b=='Wed'):
    print("Today is wednesday")
elif(b=='Sun'):
    print("Today is sunday")
elif(b=='Mon'):
    print("Today is Monday")
elif(b=='Tue'):
    print("Today is Tuesday")
elif(b=='Thu'):
    print("Today is thursday")
elif(b=='fri'):
    print("Today is friday")
elif(b=='Sat'):
    print("Today is saturay")
else:
    print("today?")
