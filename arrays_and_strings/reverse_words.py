"""
Write a function that reversts the order of ther words in a string.
For example, your function should transform the string
"Do or do not, there is no try." to "try. no is there not, do or Do".
Assume that all words are space delimeted and treat punctuation the same as letters.
"""

def reverse_words(sentence):
    """
        Solution consists of a linear reversed sweep across of the string,
        adding words found to a buffer and joining the buffe again
    """
    length = len(sentence)
    rev_sentence = []

    end = length

    for index in reversed(range(length)):
        if sentence[index] == ' ':
            rev_sentence.append(sentence[index+1:end])
            end = index

    rev_sentence.append(sentence[0:end])

    return ' '.join(rev_sentence)

if __name__ == "__main__":
    print reverse_words("Do or do not, there is no try.")
