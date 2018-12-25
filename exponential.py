# this program is to implement the e^x


import math


def e(x, accuracy):
    i = 1
    y = x



    z = float(0)
    r=float(0)
    value = float(0)

    try:
        while i<accuracy:


            q=math.pow(x,i)
            w=math.factorial(i)



            r=q/w

            z=z+r

            i = i + 1


    except OverflowError as err:
        print("overflow happend at i:",i)


    value = z + 1

    return value


