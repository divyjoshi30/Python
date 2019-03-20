def food():     #define a function
    print("Milk and Cheese")
food()   #calling a function
print(food())    #it call  the funcition but prints none bcs we haven't defined any parameter

def food():
    width = 80
    text = "Milk and Cheese"
    left_margin = (width - len(text))  // 2
    print(" " * left_margin, text)
food()

def center_text(text):
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)