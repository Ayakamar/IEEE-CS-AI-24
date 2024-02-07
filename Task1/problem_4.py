def reverses(sentence):
    reversed_sentence = sentence[::-1]
    return reversed_sentence

sentence = input().split()
result = reverses(sentence)
print(*result)
