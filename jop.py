import functools

def bread(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Bulka")
        func(*args, **kwargs)
        print("Bulka")
    return wrapper

def mustard(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("ketchup")
        func(*args, **kwargs)
        print("mayones")
    return wrapper

def salad(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("salatik")
        func(*args, **kwargs)
    return wrapper

def kolbasenko(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Danil Kolbasenko")
        func(*args, **kwargs)
    return wrapper

def mem(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Blin s vetchinoy")
        func(*args, **kwargs)
    return wrapper

def blin_1 (func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Vi blini blini blini")
        func(*args, **kwargs)
    return wrapper

def blin_2 (func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Vi blinochki moi")
        func(*args, **kwargs)
    return wrapper

@mem
@blin_1
@blin_2
@kolbasenko
@salad

def make_buterbrodick():
    pass

make_buterbrodick()
