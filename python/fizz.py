def mira(i):
    
    if(i%3==0 and i%5==0):
        print("fizzbuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    elif(i%2==0):
        print(str(i))
    
        
mira(3)
mira(5)
mira(15)
mira(4)
    