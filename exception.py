prompt = "Enter a number"

while True:
    try:
        x = int(input(prompt))
        break
    except ValueError:
        print("Invalid Input...Try Again...")
        
print("+++++++++++++++")

while True:
    try:
        data = input("Enter value")
        x = int(data.split(',')[1])
        break
    except IndexError:
        print('Input atleast 2 values.')
    except ValueError:
        print("Invalid input...Please try again...")
        
print("+++++++++++++++")

data = input()
try:
    x = int(data.split(',')[1])
except (ValueError, IndexError):
    print("Invalid Input...")
    
print("+++++++++++++++")

while True:
    try:
        data = input("Enter num")
        x = int(data.split(',')[1])
    except (ValueError, IndexError):
        print("Invalid Input...")
    else:
        print("All is Well ! ")
        break
        
print("=================")

def f(x):
    try:
        y = int(x)
        return y
    except ValueError:
        print(x)
    finally:
        print("Finally")
f(5)
#output --> Finally
            # 5
            
print("=================")

def f(x):
     return x + 2
     
     
def safe_run(f, x):
    try:
        f(x)
    except ValueError:
        return 'ValueError'
    except TypeError:
        return 'TypeError'
    else:
        return 'OK'
#output --> safe_run(2, 7)
            #'TypeError'
            
print("=================")

def func(x):
    if type(x) != int:
        raise TypeError('Expected int')
    elif x < 0:
        raise ValueError('Got negative int')
    

#output --> 1) func('hii')
            # TypeError: Expected int
            
#output --> 2) func(-7)
            # ValueError: Got negative int
            
#output --> 3) func(4)
            # correct answer