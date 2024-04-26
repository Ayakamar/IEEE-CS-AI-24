def determine_photo_type():
   
    n, m = map(int, input("Enter the number of rows and columns: ").split())
    
    colored_pixels = {'C', 'M', 'Y'}
    
    is_colored = False
    
    for _ in range(n):
     
        row_colors = input("Enter the colors for the row, separated by space: ").split()
      
        for color in row_colors:
            if color in colored_pixels:
                is_colored = True  
                break  
        if is_colored:
            break
 
    if is_colored:
        print("#Color")
    else:
        print("#Black&White")

determine_photo_type()
