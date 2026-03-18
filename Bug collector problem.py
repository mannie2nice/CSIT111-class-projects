# Emmanuel Adisa
# 03/08/2026

#initialize the accumulator
total = 0

#Get the bugs collected for each day
for day in range (1,8):
    print("Enter the bugs collected on day", day)
    bugs = int(input ())
    total += bugs
    
    #Display the total bugs.
    print("you collected a total of", total, "bugs")
    

#get bugs
total = int(input("how much bugs did u collect?"))
    
#calculate bugs
if total > 50:
    print("thats a lot of bugs")
else:
    print("have a nice day")