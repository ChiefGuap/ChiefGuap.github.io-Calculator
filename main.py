print("Hello! Im a nice trusty calculator! I can do basic operations of Math")
print("[1]:Addition")
print("[2]:Subtraction")
print("[3]:Multiplication")
print("[4]:Division")
print("[5]:Exponential")
operation = input("Please select a number on which operation you want to do?:")


if operation == "4" :
  print("Division Calculator")
  Division_1 = float(input("Enter your first number:"))
  Division_2 = float(input("Enter your second number:"))
  Answer_D = Division_1 / Division_2
  print("Your answer is: " + str(Answer_D))

else:

      if operation == "3" :
        print("Multiplication Calculator")
        Multiplication_1 = float(input("Enter your first number:"))
        Multiplication_2 = float(input("Enter your second number:"))
        Answer_M = Multiplication_1 * Multiplication_2
        print("Your answer is: " + str(Answer_M))

      else:

          if operation == "2" :
            print("Subtraction Calculator")
            Sub_1 = float(input("Enter your first number:"))
            Sub_2 = float(input("Enter your second number:"))
            Answer_S = Sub_1 - Sub_2
            print("Your answer is: " + str(Answer_S))

          else:

            if operation == "1" :
              print("Addition Calculator")
              Add_1 = float(input("Enter your first number:"))
              Add_2 = float(input("Enter your second number:"))
              Answer_A = Add_1 + Add_2
              print("Your answer is: " + str(Answer_A)) 
            
            else:

              if operation == "5":
                print("exponential calculator")
                ex_1 = float(input("What is the base of the exponent:"))
                ex_2 = float(input("What power do you want to raise it to:"))
                Answer_E = ex_1 ** ex_2
                print("Your answer is: " + str(Answer_E))

              else:

                for  i in range (operation > "5"):
                  print("Invalid operation! Please retype a valid number. :)")  
                  if operation == "3" :
                    print("Multiplication Calculator")
                    Multiplication_1 = float(input("Enter your first number:"))
                    Multiplication_2 = float(input("Enter your second number:"))
                    Answer_M = Multiplication_1 * Multiplication_2
                    print("Your answer is: " + str(Answer_M))
                  else:
                    if operation == "2" :
                      print("Subtraction Calculator")
                      Sub_1 = float(input("Enter your first number:"))
                      Sub_2 = float(input("Enter your second number:"))
                      Answer_S = Sub_1 - Sub_2
                      print("Your answer is: " + str(Answer_S))

                else:

                    if operation == "1" :
                      print("Addition Calculator")
                      Add_1 = float(input("Enter your first number:"))
                      Add_2 = float(input("Enter your second number:"))
                      Answer_A = Add_1 + Add_2
                      print("Your answer is: " + str(Answer_A)) 
            
                    else:

                      if operation == "5":
                        print("exponential calculator")
                        ex_1 = float(input("What is the base of the exponent:"))
                        ex_2 = float(input("What power do you want to raise it to:"))
                        Answer_E = ex_1 ** ex_2
                        print("Your answer is: " + str(Answer_E))  


           

    
                
