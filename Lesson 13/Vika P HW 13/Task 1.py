def func1():
    a = 5
    def func2():
        b = 10

    def func3():
        c = 10

    var = dir()
    print('Local variables in this functions are: ', var)
    print('Nunber of local variables: ', len(var))

func1()






