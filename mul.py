def make_multiplier(factor):
    def multiply(x):
         return x * factor

    return multiply


times10 = make_multiplier(10)
print(times10(2))  
print(times10(7)) 

double = make_multiplier(2)
print(double(5))  

print(make_multiplier(10)(2))