def binary_Search(seq, low, high):
    firstSeqPlace = 0
    seqLen = len(seq)
    lastSeqPlace = seqLen - 1
    if low >= high:
        raise ValueError ("The 'low' value can not be bigger then 'high' value")
    while firstSeqPlace <= lastSeqPlace and True:
        middleValue = seqLen // 2
        if seq[middleValue] in range (low, high+1):
            return (True)
        else:
            if seq[middleValue] < low:
                return (binary_Search(seq[middleValue+1:], low, high)) #checks first half of the sequence
            else:
                return (binary_Search(seq[:middleValue], low, high)) #else checks second half of the sequence 
        
                


seq = [2,3,5,7,9,13]
low = 10
high = 14
biSearch = binary_Search(seq, low, high)
print (biSearch)
