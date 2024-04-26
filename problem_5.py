def game_scores(cards):
    sereja_score = 0
    dima_score = 0
    left = 0
    right = len(cards) - 1
    turn = 0 
    while left <= right:
       
        if cards[left] > cards[right]:
            if turn == 0:  
                sereja_score += cards[left]
                left += 1
            else: 
                dima_score += cards[left]
                left += 1
        else:
            if turn == 0:  
                sereja_score += cards[right]
                right -= 1
            else:  
                dima_score += cards[right]
                right -= 1

        turn = 1 - turn

    return sereja_score, dima_score

n = int(input("Enter the number of cards: "))  
cards = list(map(int, input("Enter the card values separated by space: ").split()))  

sereja_score, dima_score = game_scores(cards)

print(f"Sereja's score: {sereja_score}, Dima's score: {dima_score}")
