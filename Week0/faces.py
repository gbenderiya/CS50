def main():
    faces()
    
def faces():
    face = input("What's your input:")
    face = face.replace(":)","😊")
    face = face.replace(":(","😠")
    print(face)
        
if __name__=="__main__":
    main()
    
    
