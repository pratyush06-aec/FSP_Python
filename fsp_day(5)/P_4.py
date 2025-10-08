class WordReverser:
    def __init__(self, words):
        # words is expected to be a list of strings
        self.words = words

    def reverse_words(self):
        n = len(self.words)
        # Swap elements from start and end moving towards the middle
        for i in range(n//2):
            # Swap element at i with the element at (n - 1 - i)
            self.words[i], self.words[n-1-i] = self.words[n-1-i], self.words[i]
        return self.words

# Example usage:
if __name__ == "__main__":
    # Taking user input as space-separated words and converting it to list
    input_words = input("Enter words separated by space: ").split()
    reverser = WordReverser(input_words)
    reversed_list = reverser.reverse_words()
    print("Reversed list:", reversed_list)

    

