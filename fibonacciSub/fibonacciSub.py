def lenLongestFibSubseq(arr):
    prev = arr[0] # The first number in the sequence
    curr = arr[1] # The second number in the sequence
    seqNo = 0 # Stores how many numbers in the fibonacci sequence
    skippedNums = []

    # Iterate throgh the array
    for i in range(2, len(arr)):

        total = prev + curr
        # Checks if the sum of the two number is equal to the next number in the list
        if total == arr[i]: 
            prev = curr # Assign the previous number to the current number
            curr = arr[i] # Assign the current number to the new number found in the sequence
            
            # Checks if the sequence started or not and add number accordengly
            if seqNo > 0:
                seqNo += 1 # Increment the length of the fibonacci sequence
            else:
                seqNo = 3 # Assign the innitial fibonacci sequence numbers to 3 since the fibonacci sequence needs atleast three numbers
        
        elif total < arr[i]:
            prev = curr
            curr = arr[i]
        
        else:
            continue


    return seqNo

if __name__ == "__main__":
    print(lenLongestFibSubseq([int(n) for n in input("Write positive accending numbers from atleast 1: ").split()]))