def main():
    camelCase()
    
def camelCase():
    camel = input("camelCase: ") 
    print("snake_case: ", end="")
    for i in camel:
        if i.isupper():
            print("_"+i.lower(), end = "", sep ="")
        else:
            print(i, end = "")
            
main()