# Emmanuel Adisa
# 2/18/2026

print("Hey kids, my name is funculator, here you can enter the length & width of your rectangle and i'll work the magic and tell you which rectangle has the greater area ;) ")

name = input ("First, what is your name? ")

print("Pleasure to meet you", name)

print("Alright now enter the length & width of rectangle one. ")

length1 = int(input("Rectangle 1's length: ")) 
width1 = int(input("Rectangle 1's width: "))
rectangle1 = length1 * width1

print("Great job! now enter the length & width of rectangle two. ")

length2 = int(input("Rectangle 2's length: "))
width2 = int(input("Rectangle 2's width: "))
rectangle2 = length2 * width2

area1 = rectangle1
area2 = rectangle2

if area1 > area2:
    print("Nice "+name+"! Rectangle 1 has the greater area. ")
elif area2 > area1:
        print("Wonderful "+name+"! Rectangle 2 has the greater area. ")
else:
            print("Perfect "+name+"! They both have the same area. ")