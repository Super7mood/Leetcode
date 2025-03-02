def lenLongestFibSubseq(arr):
        
        for i in range(len(arr)):
            fibTotal = arr[i] # contains the number in fibonacci sequence
            fibList = [arr[i]] # Contains the number in the list
            fibNum = 0 # The amount of number in a sequence
            
            for j in (i + 1 , len(arr) - 1):
                fibTotal += arr[j]
                if fibTotal in arr:
                    fibList.append(arr[j])
                    fibList.append(fibTotal)
                    fibNum += 2
        

        print(fibList)
        return fibNum


if __name__ == "__main__":
    lenLongestFibSubseq([int(n) for n in input("Write positive accending numbers from atleast 1: ").split()])