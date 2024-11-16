def check_age():
    while True:
        try:
            
            age = int(input("Please enter your age: "))
            
            if age < 0:
                print("Error: Age cannot be negative. Please enter a valid age.")
                continue 

        
            if age % 2 == 0:
                print(f"Your age is {age}, which is even.")
            else:
                print(f"Your age is {age}, which is odd.")
            break  
            
        except ValueError:
        
            print("Error: Please enter a valid integer for your age.")

check_age()
