class CustomException(Exception):
    pass

def divide_numbers():
    try:
        # Get inputs from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Check for zero division
        if num2 == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero")

        # Perform division
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

        # Simulate a runtime error for demonstration
        if result == 2:
            raise RuntimeError("Simulated Runtime Error")

        # Simulate a custom exception for demonstration
        if result == 3:
            raise CustomException("Simulated Custom Exception")

    except ZeroDivisionError as zd_error:
        print(zd_error)
    except RuntimeError as rt_error:
        print(rt_error)
    except CustomException as custom_error:
        print(custom_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Division successful.")
    finally:
        print("Program execution complete.")

if __name__ == "__main__":
    divide_numbers()
