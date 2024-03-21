def bayes_theorem(prior_a, prior_b, conditional_b_given_a):
    probability = (prior_a * conditional_b_given_a )/prior_b
    return probability

try:
    
    prior_a = input("Enter the prior probability of event A : ")
    prior_b = input("Enter the prior probability of event B : ")
    conditional_b_given_a = input("Enter the conditional probability of B given A : ")

    prior_a = float(prior_a)
    prior_b = float(prior_b)
    conditional_b_given_a = float(conditional_b_given_a)
        
        
    if not 0 <= prior_a <= 1 or not 0 <= prior_b <= 1 or not 0 <= conditional_b_given_a <= 1:
        raise ValueError("Probabilities must be between 0 and 1.")
        
    result = bayes_theorem(prior_a, prior_b, conditional_b_given_a)
    print(result)
except Exception as e:
    print(f"An unexpected error occurred: {e}")