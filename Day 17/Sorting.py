# HackerRank

'''

Today, we're discussing a simple sorting algorithm called Bubble Sort. Check out the Tutorial tab for learning materials and an instructional video!

Consider the following version of Bubble Sort:

for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}
Task
Given an array, , of size  distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following  lines:

Array is sorted in numSwaps swaps.
where  is the number of swaps that took place.
First Element: firstElement
where  is the first element in the sorted array.
Last Element: lastElement
where  is the last element in the sorted array.
Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.

Input Format

The first line contains an integer, , denoting the number of elements in array .
The second line contains  space-separated integers describing the respective values of .

Constraints

, where .

Output Format

Print the following three lines of output:
Array is sorted in numSwaps swaps.
where  is the number of swaps that took place.
First Element: firstElement
where  is the first element in the sorted array.
Last Element: lastElement
where  is the last element in the sorted array.

Sample Input 0
3
1 2 3

Sample Output 0
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
'''

# !/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
def bubble(arr):
    count_swap = 0
    for num in range(len(arr)-1, 0, -1):
        for i in range(num):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count_swap +=1
    return count_swap

print ("Array is sorted in {} swaps.".format(bubble(a)))
print ("First Element: {}".format(a[0]))
print ("Last Element: {}".format(a[-1]))