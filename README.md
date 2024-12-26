# Harvard CS50 (2023) – Full Computer Science University Course

Th repo contains the solution to the problem sets.
Here is agenda:
Week 0: Functions, Variables
Week 1: Conditionals
Week 2: Loops
Week 3: Exceptions
Week 4: Libraries
Week 5: Unit Tests
Week 6: File I/O
Week 7: Regular Expressions
Week 8: Object-Oriented Programming
Et Cetera

## Week0
### Indoor Voice
```
InVoice = input("Use your indoor voice! ").lower()
print(InVoice)
```

### Playback Speed
playbackspd = input("Display 0.75 playback speed ").split()
print('...'.join(playbackspd))

### Playback Speed
playbackspd = input("Display 0.75 playback speed ").split()
print('...'.join(playbackspd))

### Making Faces
def main():
    faces()
    
def faces():
    face = input("What's your input:")
    face = face.replace(":)","😊")
    face = face.replace(":(","😠")
    print(face)
        
if __name__=="__main__":
    main()

### Einstein
def main():
    einstein()
    
def einstein():
    m = int(input("m: "))
    c = 300000
    e = m*c**2
    print(e)

if __name__ == "__main__":
    main()
    
### Tip Calculator
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
    
def dollars_to_float(d):
    d = d.replace("$","")
    return float(d)

def percent_to_float(p):
    p = p.replace("%","")
    p = float(p)
    p = p/100
    return p
main()

## Week1
