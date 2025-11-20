def my_decorator(func):
    def wrapper(a,b):
        res=func(a,b)
        if res%2!=0:
            return res*2
        else:
            return res
    return wrapper
@my_decorator
def add(a,b):
    return a+b
print(add(2,3))   
print(add(2,4))