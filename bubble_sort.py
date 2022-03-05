import re

# To keep track of how many iterations have been completed
iterations = 0

def bubble_sort(arr):
    """Sort array of strings in bubble fasion"""
    global iterations
    # location and value of last word
    lastA = (0, "")
    # location and value of last number
    lastN = (0, "-1000000")
    # indicates True there have been switches in the array
    switched = False

    for a in enumerate(arr):
        # If the algorithm has already reached the the right end element continue
        if a[0] > len(arr) - (iterations + 1):
            continue
        if a[1].lstrip('-').isalpha():
            # Remove dash from beginning of string if it exists
            arr[a[0]] = a[1].lstrip('-')
            # Swap the locations of the words if the last word is greather than the current word
            if lastA[1] > a[1].lstrip('-'):
                arr[lastA[0]] = a[1]
                arr[a[0]] = lastA[1]
                # Set the last number variable to the new location of the last word
                lastA = (a[0], lastA[1])
                switched = True
            # Set the last word if no numbers and there was no switch
            else:
                lastA = a
        elif a[1].lstrip('-').isnumeric():
            # Swap the locations of the words if the last number is greather than the current number
            if int(lastN[1]) > int(a[1]):
                arr[lastN[0]] = a[1]
                arr[a[0]] = lastN[1]
                # Set the last number variable to the new location of the last number
                lastN = (a[0], lastN[1])
                switched = True
            # Set the last word if just numbers and there was not a switch
            else:
                lastN = a
    iterations += 1

    # If There have been switches sort again otherwise return
    if switched:
        bubble_sort(arr)
    else:
        return