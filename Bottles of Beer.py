"""Write the program "99 Bottles of Beer on the Wall" using a while loop. Be mindful to change the word 'bottles' to 'bottle'
 when down to the last one. You must do the full 99 bottles; the sample shows the last 3 verses"""

print() #Empty line for visual clarity
bottles = 99 
while bottles > 0: #While bottles is more than zero, it will run.
    if bottles > 2: #If greater than two, it will count down normally, if not...
        print(f"{bottles} bottles of beer on the wall!")
        print(f"{bottles} bottles of beer!")
        print("Take one down, pass it around")
        bottles -= 1
        print(f"{bottles} bottles of beer on the wall!\n")
    elif bottles == 2:
        print(f"{bottles} bottles of beer on the wall!")
        print(f"{bottles} bottles of beer!")
        print("Take one down, pass it around")
        bottles -= 1
        print(f" Only {bottles} bottle of beer on the wall!\n") #Singular bottle starting here.
    elif bottles == 1:
        print(f"{bottles} bottle of beer on the wall!")
        print(f"Only {bottles} bottle of beer!")
        print("Take one down, pass it around")
        bottles -= 1
        print("No more bottles of beer on the wall!!!!\n") #Bottles changes back to plural here.
    #Not necessary to close off with an else statement.