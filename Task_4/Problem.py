def get_numbers():
    number = []
    try:
        num = input("Enter numbers separated by spaces :\n")
        num_list = num.strip().split() 
        number = [float(num) for num in num_list] 
        numbers= sorted(number)
    except ValueError as e:
        print(f"Invalid input! {e}")
    return numbers
 
# function to find the minimum number
def find_min(numbers):
     
    return numbers[0]

# function to find the maximum number
def find_max(numbers):
   
    return numbers[len(numbers)-1]

def find_mean(numbers):
    sum_list = sum(numbers)
    # the mean is the total number divided by counting of number
    mean = sum_list / len(numbers)
    return mean

# function to find the mode  
def find_mode(numbers):
    # check if the variable numbers not empty or not number may be a string or word not number 
    if not numbers:
        return []
    freq_dict = {}
    for num in numbers:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    max_freq = max(freq_dict.values())
    for num,freq in freq_dict.items():
        if freq == max_freq:
            mode = num
    return mode 

# the median is the number that exist in the middle of the list n 
def find_median(numbers):
    n = len(numbers) 
    if n % 2 == 0:
        #median =  take the sum of the two number divied by 2
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
    # if the number is odd so the number is exist in the middle 
        median = numbers[n // 2]
    return median

# range function 
def find_range(numbers):
    # we use try and catch to handle the error and avoid bugs 
    try:
        min_num = min(numbers)
        max_num = max(numbers)
        return max_num - min_num
    except ValueError:
        print("Error: Unable to calculate range. Please ensure you have provided valid numeric input.")
        return None

# variance function 
def find_variance(numbers):
    if not numbers:
        print("No numbers to calculate variance.")
        return None
    # the variance function is calculated by the average of squared differences of mean 
    mean = find_mean(numbers)
    sum = 0
    for num in numbers:
        sum += (num - mean) ** 2
    return sum / len(numbers)


# standared deviation function 
def find_std(numbers):
    # standard deviantins is the square root of variance
    variance = find_variance(numbers) 
    std = variance ** 0.5
    return std


# calculates the quartiles of a dataset
def find_quartiles(numbers):
    # error handling handling, and avoid bugs with displaying the error on message to user
    try:
        sorted_numbers = sorted(numbers)
        n = len(numbers)
        Q1_index = n // 4
        Q2_index = n // 2
        Q3_index = (3 * n) // 4
        Q1 = sorted_numbers[Q1_index]
        Q2 = sorted_numbers[Q2_index]
        Q3 = sorted_numbers[Q3_index]
        return Q1, Q2, Q3
    except IndexError:
        print("Error: Not enough numbers to calculate quartiles.")
        return None, None, None
    
# calculates the Interquartile Range (IQR) of a dataset
def find_iqr(numbers):
    try:
        Q1, _, Q3 = find_quartiles(numbers)
        iqr = Q3 - Q1
        return iqr
    except Exception as e:
        
        print(f"Error calculating IQR: {e}")
        return None


def main():
    numbers = get_numbers()
    
    print("Min:", find_min(numbers))
    print("Max:", find_max(numbers))
    print("Mean:", find_mean(numbers))
    print("Mode:", find_mode(numbers))
    print("Median:", find_median(numbers))
    print("Range:", find_range(numbers))
    print("Variance:", find_variance(numbers))
    print("Standard Deviation:", find_std(numbers))
    print("Quartiles:", find_quartiles(numbers))
    print("Interquartile Range (IQR):" , find_iqr(numbers))

if __name__ == "__main__":
    main()



