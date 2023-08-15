try:
    print(x)
except:
    print("An except occurred")

try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something went wrong")


try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")







