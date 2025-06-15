def safe_divide(numerator, denominator):
    try:
       numerator = float(numerator)
       denominator = float(denominator)
       
       
       if denominator == 0:
           raise ZeroDivisionError(denominator)
    except ZeroDivisionError as e:
        return "Error: Cannot divide by zero."
    except ValueError as e:
        
       return "Error: Please enter numeric values only."
    
    except Exception as e:
        return "Invalid input"
    else:
        return f"The result of the division is {numerator / denominator}"
       
        

        