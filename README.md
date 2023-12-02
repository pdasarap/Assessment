# Assessment
# Approach:
1. Created a helper function - reverseArray - to reverse the given array from given left to right.
2. leftRotateArray function which takes in array of integers and k - updates array each time it calls the reverseArray function
3. Conditions:
    - if k<0: returns error message: "Negative k is not accepted"
    - else: k=k%n - to handle any positive value of k (i.e. k<=n or k>n)
4. arr input takes in any sorted or unsorted array and returns the left-rotated array

# Complexity Analysis:
1. Time Complexity: O(n) 
    - three calls to helper function which is three while loops are run but each iterates through less than n elements each time - covering n elements twice 
    - which would be O(2n)->O(n)
2. Space Complexity: O(1)
    - Not using any extra space to hold the array of n elements. changes are made inplace.
    - Used constant extra space.
