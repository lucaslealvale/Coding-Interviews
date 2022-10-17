T9_CHARS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

def get_valid_t9_words(number, word_set):
    results = []

    def get_valid_words(number, prefix):
        # If it's a complete word, print it.
        if not number:
            if prefix in word_set:
                results.append(prefix)
            return

        # Get characters that match this digit.
        digit = number[0]
        letters = T9_CHARS.get(digit, '')

        # Find in https://stackoverflow.com/questions/14617569/check-if-any-members-of-a-set-start-with-a-given-prefix-string-in-python
        if(any(x.startswith(prefix) for x in word_set)):
        
            # Go through all remaining options.
            for letter in letters:
                get_valid_words(number[1:], prefix + letter)
           

    get_valid_words(number, '')
    return results
