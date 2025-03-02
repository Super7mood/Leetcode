def lenLongestFibSubseq(arr):
    prev = arr[0] # The first number in the sequence
    prevIndex = 0 # Stores the position of the previous number

    curr = arr[1] # The second number in the sequence
    currIndex = 1 # Stores the position of the current number

    seqNo = 0 # Stores how many numbers in the fibonacci sequence
    tempSeqNo = 0
    combinationQueue = []

    # Iterate throgh the array
    i = 2
    while i < len(arr) + 1:

        # Checks if there is still combinations of the sequence we didn't iterate and check
        if i == len(arr) and len(combinationQueue) > 0:
            prevIndex, currIndex = combinationQueue.pop(0) # Assign the indexes
            i = currIndex + 1 if currIndex != len(arr) - 1 else currIndex
            prev = arr[prevIndex] 
            curr = arr[currIndex]
            if seqNo > tempSeqNo:
                tempSeqNo = seqNo
            seqNo = 0
        
        elif i == len(arr):
            break

        total = prev + curr # Get the sum of the numbers

        # Checks if the sum of the two number is equal to the next number in the list
        if total == arr[i]: 
            prev = curr # Assign the previous number to the current number
            prevIndex = currIndex
            curr = arr[i] # Assign the current number to the new number found in the sequence
            currIndex = i

            # Checks if the sequence started or not and add number accordengly
            if seqNo > 0:
                seqNo += 1 # Increment the length of the fibonacci sequence
            else:
                seqNo = 3 # Assign the innitial fibonacci sequence numbers to 3 since the fibonacci sequence needs atleast three numbers
        
        elif total < arr[i]:
            combinationQueue.append((prevIndex, i))
            prev = curr
            prevIndex = currIndex
            curr = arr[i]
            currIndex = i
        
        if seqNo > tempSeqNo:
            tempSeqNo = seqNo
        
        i += 1


    seqNo = tempSeqNo
    return seqNo

if __name__ == "__main__":
    print(lenLongestFibSubseq([int(n) for n in input("Write positive accending numbers from atleast 1: ").split()]))