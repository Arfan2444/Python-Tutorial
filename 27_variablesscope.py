# variable scope - where a variable is visible and accessible
#  scope resolution - LEGB local -> Enclosed -> Global -> Builtin

name = "Arfan Pathan"

def fun1():
    # These variables have local scope meaning only visible within function eg a,b
    a = 1
    print(a)

def fun2():
    b = 2
    print(b)

fun1()
fun2()


def func1():
    x = 4
    # now here since no local variable x is available in func2() then it will search in enclosed scope
    def func2():
        print(x)
    func2()

func1()

# since there is no local or enclosed version of name variable available it will search in global scope
def printname():
    print(name)

printname()