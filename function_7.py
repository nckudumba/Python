n = 1    #GLOBAL VARIABLE


def fn():
    #global n
    n = 5   #LOCAL VARIABLE                 
    print('in',n)

fn()



print('out',n)


#LOCAL VARIBALE IS CONSIDERED THE HIGHEST THAN A GLOBAL VARIABLE (IMPORTANT)