def reverseWords(sentences):
    joined_string =[]

    for i in sentences.split():
        joined_string.append(i[::-1])
    
    return " ".join(joined_string)

