def hello(name):
    print(f"HI, {name}")

hello("ED")

def add(a, b):
    return a + b


res = add(1, 2)
print("Sum: ", res)

def power(base, exp=2):
    return base ** exp

print("2^3: ", power(2, 3))
print("2^2: ", power(2))

def concatenate(*args):
    r = ""
    for arg in args:
        r += arg
    return r

print (concatenate("hi, " , "World"))
print (concatenate("Python", " ", " is" "amazing"))