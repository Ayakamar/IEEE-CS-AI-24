if __name__ == '__main__':
    records = []
    score_list = []
    name_list = []
    
    for _ in range(int(input())):
        student_name = input()
        student_score = float(input())
        score_list.append(student_score)
        records.append([student_name, student_score])
    
    # Sort the scores list
    score_list.sort()

    # Find the second lowest score
    second_score = sorted(set(score_list))[1]
     
    student_with_second_score = []
    for i in range(len(records)):
        if records[i][1] == second_score:
            student_with_second_score.append(records[i][0])  
            
    for name in student_with_second_score:
        name_list.append(name)
   
    name_list.sort()
   
    for name in name_list:
        print(name)

        
