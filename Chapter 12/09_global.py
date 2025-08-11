a = 89

def fun():
    global a  #global wala change kar dega
    a = 3
    print(a)
    
fun()
print(a)