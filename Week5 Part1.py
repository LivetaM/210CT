def longest_Sub_Seq(seq):
    maximum = 0
    new_List = []
    for x in seq:
        if x > maximum:
            maximum=x #if statment is met it assigns maximum to x
            new_List.append(maximum) #creates the list of longest sub-sequence
    return (new_List) 

print (longest_Sub_Seq([1,1,2,3,4,1,2]))
            

#http://stackoverflow.com/questions/40667713/extracting-the-subsequence-of-maximum-length-from-a-sequence-python
