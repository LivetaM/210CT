def reverse_Words(sentence):
    splitted_Sentence = sentence.split()
    sen_Len = len(splitted_Sentence)
    new_Sentence = []
    for new in range  (1, sen_Len+1):
        if sen_Len <= 1:
            return (sentence)
        else:
            new_Sentence.append(splitted_Sentence[sen_Len-new]) #appends words backwards from splitted sentence to the start of new list     
    return (" ".join(new_Sentence)) #connects words in the list with spaces, to make it into one sentence

print (reverse_Words("This is awesome"))
            
