original_price = float(input("Enter the original price: "))
selling_price = float(input("Enter your selling price: ")) 
if selling_price > original_price:
    print("You made a profit")
elif selling_price < original_price:
    print("You made a loss")
else:
    print("You made neither a profit nor a loss.")
    
    