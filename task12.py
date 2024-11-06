def dictionary(sentence):
    dictionary_symbols = {}
    for symbol in sentence:
        if symbol in dictionary_symbols:
            dictionary_symbols[symbol] += 1
        else:
            dictionary_symbols[symbol] = 1
    return dictionary_symbols

word = 'Hello world!'
result = dictionary(word)

print(result)