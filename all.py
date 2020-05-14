def generator(b):    
    for i in range(b+1):
        yield i
        if i % 3 == 0:
            yield('Вася')
            
            
            
        
r = generator(100)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))