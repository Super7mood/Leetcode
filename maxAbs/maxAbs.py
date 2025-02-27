# This function finds the maximum absolute sum of all the subarrays in a list
def maxAbsoluteSum(nums):
    
    maxPrefix = 0 # Stores the largest value recoreded of the sum of the numbers
    minPrefix = 0 # Stores the Smallest value recorded of the sum of the numbers
    sumPrefix = 0 # Stores the sum of the numbers

    # Iterate throgh the numbers
    for num in nums:
        sumPrefix += num # Add the number to the sumPrefix

        maxPrefix = max(maxPrefix, sumPrefix) # Check if sumPrefix is bigger than maxPrefix
        minPrefix = min(minPrefix, sumPrefix) # Check if sumPrefix is smaller than minPrefix

    return maxPrefix - minPrefix # return max - min, which shows the largest absolute maximum subArray sum

if __name__ == "__main__":
    
    print(maxAbsoluteSum([int(n) for n in input("Enter number seperated by spaces: ").split()]))