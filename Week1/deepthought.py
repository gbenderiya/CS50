def main():
    dt()
    
def dt():
    din = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    
    if din.lower() == 'forty-two' or din.lower() == 'forty two' or din.lower() == '42':
        print('Yes')
    else:
        print('No')
        
if __name__ =='__main__':
    main()
        