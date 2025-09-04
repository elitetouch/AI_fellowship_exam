# question 1

# Basic Calculator
while True:
    first_number = input("Enter first number  (or type 'exit' to quit): ")
    
    if first_number == "exit":
        print("Exiting calculator... Goodbye!")
        break       # break out of loop
    second_number = input("Enter second number (or type 'exit' to quit): ")
    if second_number == "exit":
        print("Exiting calculator... Goodbye!")
        break       # break out of loop

    print("operations")
    print("1. Addition (+)\n2. Substraction(-)\n3. Multiplication(*)\n4. Division(/)")

    operation = input("Choose operation (+, -, *, /) by entering  (1,2,3, or 4 ) or type 'exit' to quit ): ")

    if operation == "exit":
        print("Exiting calculator... Goodbye!")
        break       # break out of loop




    def add_num(first_number,second_number,operation):

        try :
            if operation == '1':
                sum = int(first_number) + int(second_number) 
                print(f'Result: {sum}')
                # return sum
        except:
            print("Invalid input")

    def subtract_num(first_number,second_number,operation):
        try:
            if operation == '2':
                sum = int(first_number) - int(second_number) 
                print(f'Result: {sum}')
                # return sum
        except:
            print("Invalid input")

    def multiply_num(first_number,second_number,operation):
        try:
            if operation == '3':
                sum = int(first_number) * int(second_number) 
                print(f'Result: {sum}')
                # return sum
        except:
            print("Invalid input")            

    def divide_num(first_number,second_number,operation):
        try:
            if operation == '4':
                if int(first_number) != 0:
                    sum = int(first_number) / int(second_number) 
                    # return sum
                    
                else:
                    print(f'Error: Cannot divide by zero')
        except:
            print("Invalid input")       

    add_num(first_number,second_number,operation)       
    subtract_num(first_number,second_number,operation)     
    divide_num(first_number,second_number,operation)   
    multiply_num(first_number,second_number,operation)




#question 2
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break       # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")




# # question 3
while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == 'exit':
        print("Goodbye!")
        break
    
    try:
        age = int(age)
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")