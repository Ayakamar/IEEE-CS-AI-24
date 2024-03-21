def probability_distribution(the_list):
    n = len(the_list)
    probability_distribution = {}
    
    for value in the_list:
         
         try:
            value = int(value)  
         except ValueError:
            raise ValueError("All values must be integers.")
         
         if value in probability_distribution:
             probability_distribution[value] += 1 / n
         else:
             probability_distribution[value] = 1 / n
    
    return probability_distribution
try:
    the_list = input("Enter the list of values separated by spaces: ").split()
    if not the_list:
        raise ValueError("List is empty.")
    
    result = probability_distribution(the_list)
    print(result)
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")




