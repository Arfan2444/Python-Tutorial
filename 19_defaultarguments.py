# default arguments - A default value for certain parameters
#                     default is used when that argument is omitted
#                     makes your functions more flexible, reduces # of arguments
import time

def net_price(listprice,discount = 0,tax = 0.05):
    return listprice * (1-discount) * (1+tax)

print(net_price(500,0.1))


def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done")

count(30,15)

