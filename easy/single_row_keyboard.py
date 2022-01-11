def single_row_keyboard(keyboard,word):
    char_int ={}
    temp,result =0,0

    for i in range(len(keyboard)):
        char_int[keyboard[i]] =i

    for w in word:
        result +=abs(char_int[w]-temp)
        temp = char_int[w]

    return result



    