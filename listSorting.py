from bubble_sort import bubble_sort
import re
import sys

def clean_string(stringToClean):
    """Remove not alphanumeric characters except spaces with dashes (for negative numbers)"""
    negativesRemoved = re.sub(r'[^a-zA-Z0-9 -]', '', stringToClean).replace(" -", " %")
    return re.sub(r'[^a-zA-Z0-9 %]', '', negativesRemoved).replace(" %", " -")

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    cleanedStr = clean_string(f.read())
    # Split by spaces into array 
    arr = cleanedStr.split(" ")
    bubble_sort(arr)
    f = open(sys.argv[2], "w")
    f.write(" ".join(arr))
    f.close()