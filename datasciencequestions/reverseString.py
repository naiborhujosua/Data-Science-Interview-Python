def reverseString(sentence):
    return "".join(sentence[-i] for i in range(1,len(sentence)+1))

sentence = "I love programming in Python"
print(reverseString(sentence))