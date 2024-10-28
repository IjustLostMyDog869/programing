weight = int(input("Enter weight in kilograms: ")) 
len = int(input("Enter length in centimeters: "))
wid = int(input("Enter width in centimeters: "))
height = int(input("Enter height in centimeters: "))
vol = len * wid * height

if vol < 100000:
    print("Package Accepted")
elif weight < 27:
    print("Package Accepted")
elif vol > 100000:
    print("Too Heavy")
elif weight > 27:
    print("Too Big")
    
    
    
input()
    
    