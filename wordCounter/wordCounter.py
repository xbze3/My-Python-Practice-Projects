userData = input("Enter data: ").split()

def counter(arr):

    currentWordCount = 0

    for ele in arr:
        currentWordCount += 1

    print(f"Word count is {currentWordCount}")

counter(userData)