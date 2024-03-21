def conditional_probability(A, B):
    count = 0
    for i in range(len(B)):
        try:
             A[i] = int(A[i])
             B[i] = int(B[i])     
        except ValueError:
                raise ValueError("All values must be integers.")
        if A[i] == 1:
            if B[i] == 1:
                count += 1
    
    return count / sum(B) 
try:
    event_A = input("Enter the list of event A: ").split()
    event_B = input("Enter the list of event B: ").split()
    if not event_A or not event_B:
        raise ValueError("List is empty.")
    if len(event_A) != len(event_B):
        raise ValueError("The lists of events must have the same length.")
    result = conditional_probability(event_A, event_B)
    print(result)
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
