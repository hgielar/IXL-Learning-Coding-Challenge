import collections

def getMinimumDifference(a, b):
    """
    Iterate over each word in the array, then iterate over each character in the
    first word.
    For each character, if its in the first word and the second word, then
    increment the counter by the difference between the number of times the
    character appears in the first word and the number of times it appears in the
    second. If the character in the first word does not appear at all in the
    second word, then increment the counter by the number of times the letter
    appeared in the first word.

    Algorithm runs in O(N) time where N is the length of the word.
    """
    differences_array = []
    for array_index, word in enumerate(a):

        if len(word) != len(b[array_index]):
            differences_array.append(-1)
            continue

        word_difference = 0

        word_1_freq = dict(collections.Counter(a[array_index]))
        word_2_freq = dict(collections.Counter(b[array_index]))

        for letter, value in word_1_freq.items():
            if letter in word_2_freq:
                word_difference += abs(word_1_freq[letter] - word_2_freq[letter])

            else:
                word_difference += value

        differences_array.append(word_difference)

    return differences_array
