# PYTHON BEGINNERS - GISHNU M
# python code for fibanocci function
# Enter the number of terms needed in the series as parameter of function

def fibanocci_n(n):
    q = list()

    i=1
    j=0
    x=0


    while 1:

        z=i+j
        i=j
        j=z
        x+=1

        q.append(z)

        if int(x)>int(n):
            break

    return q
