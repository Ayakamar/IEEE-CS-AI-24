def common_elements(set1, set2):
    return set1.intersection(set2)

if __name__ == "__main__":

     set1 = set(input("Enter elements for the first set : ").split())
           
     set2 = set(input("Enter elements for the second set: ").split())

     common_elements = common_elements(set1, set2)

     if not common_elements  :
         print("there is no common element")
        
     else:
         print("Common elements:", common_elements)