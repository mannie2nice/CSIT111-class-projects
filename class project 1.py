# Emmanuel Adisa
# 02/11/26
# pp1

name = input ("What is your name? ") 
degree = input ("What is your degree? ") 
creditsreq = int (input ("How much credits do you need for this degree? ")) 
creditstaken = int (input ("How much credits have you taken so far? ")) 

creditsleft = creditsreq - creditstaken

print("Your name is", name)
print("Your degree is", degree)
print("Credits needed to graduate =", creditsleft)
