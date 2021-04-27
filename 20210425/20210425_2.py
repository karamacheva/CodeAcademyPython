#overloading

from multipledispatch import dispatch

@dispatch(int) 
def func(a):
    rez = a**3
    print(rez)


@dispatch(int,int)
def func(a,b):
    rez=a+b
    print(rez)

@dispatch(str,str)
def func(a,b):
    rez=a+b
    print(rez)
    
@dispatch(int,int,int)
def func(a,b,c):
    rez = (a+b)*c
    print(rez)
    
func(5)
func(2,3)
func('Hello','Ekaterina')
func(3,4,5)
