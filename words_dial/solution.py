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
    for word in word_set:
        if len(word) == len(number):
            for i in range(len(number)):
                if word[i] not in T9_CHARS[number[i]]:
                    break
            else:
                results.append(word)
    return results
   
