def test():
    yield 1
    print("hello")
gen = test()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))