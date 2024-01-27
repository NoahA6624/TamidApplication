"""
Author: Noah Adelson
Title: Tamid Junior Software Engineer Application
Description: This file contains solutions to the first and fourth puzzles on the application
Puzzle 1 uses a quick sorting algorithm to add and sort to arrays and then return a specified number of elements
Puzzle 4 checks to see if a word is a palindrome by converting the string to lowercase and comparing itself to a flipped version.
"""


def array_sorter(arr1, arr2, capacity):
    #Adds two arrays together and returns the sorted version sliced to specified number of elements
    final_arr = arr1 + arr2
    return quicksorter(final_arr)[:capacity]

def quicksorter(arr):
    #Uses a recursive quick sorting algorithm to sort array and returns sorted version
    if len(arr) == 1:
        return arr
    if len(arr) == 0:
        return []
    pivot = arr[0]
    less = []
    greater = []
    for item in arr[1:]:
        if item < pivot:
            less.append(item)
        elif item >= pivot:
            greater.append(item)
    return quicksorter(less) + [pivot] + quicksorter(greater)

def isPalindrome(str):
    #Checks to see if a word is a palindrome
    return str.lower() == str[::-1].lower()
def main():
    #Prints out results of test cases for above methods
    print(array_sorter([1, 3, 5, 8], [1, 2, 3], 5))
    print(array_sorter([2, 8, 15, 30], [1, 2, 3], 2))
    print(array_sorter([1, 3, 5, 8], [1, 2, 3], 0))
    print(array_sorter([1, 3, 5, 8], [], 10))
    print(isPalindrome("Wow"))
    print(isPalindrome("wow"))
    print(isPalindrome("Tamid"))


if __name__ == '__main__':
    main()

