from mean_var_std import calculate

if __name__ == "__main__":
    try:
        user_input = input("Hello! Please enter 9 numbers separated by commas: ").split(',')

        user_input = [int(num.strip()) for num in user_input]
        
        if len(user_input) != 9:
            raise ValueError("List must contain nine numbers.")
        
        result = calculate(user_input)
        print("\nHere are the results:\n")
        for key, value in result.items():
 
            if key == "Mean":
                print(f"{key} (the average value):")
            elif key == "Variance":
                print(f"{key} (how spread out the values are):")
            elif key == "Standard Deviation":
                print(f"{key} (the square root of the variance):")
            elif key == "Max":
                print(f"{key} (the largest value):")
            elif key == "Min":
                print(f"{key} (the smallest value):")
            elif key == "Sum":
                print(f"{key} (the total sum of the values):")
            
            print(f"  - Axis 0 (columns): {value[0]}")
            print(f"  - Axis 1 (rows):    {value[1]}")
            print(f"  - Flattened:        {value[2]}")
            print("\n" + "-" * 30)
    
    except ValueError as e:
        print(e)
