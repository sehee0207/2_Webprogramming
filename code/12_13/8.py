def func1() :
    global a
    a = 10
    print("func1()에서a값%d" % a)

def func2():
    print("func2()에서a값%d" % a)

a = 20

func1()
func2()