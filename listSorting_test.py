import unittest
from listSorting import clean_string
from bubble_sort import bubble_sort

class TestSort(unittest.TestCase):

    def test_demo(self):
        fileUnsorted = open("demo.txt", "r")
        fileSorted = open("demo-sorted.txt", "r")
        cleanedStr = clean_string(fileUnsorted.read())
        arr = cleanedStr.split(" ")
        bubble_sort(arr)
        sortedStr = " ".join(arr)
        testSortedStr = fileSorted.read()
        self.assertEqual(sortedStr, testSortedStr)
        fileSorted.close()
        fileUnsorted.close()

if __name__ == '__main__':
    unittest.main()