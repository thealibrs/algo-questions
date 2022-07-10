def isPangram(sentence):
    import string 
    alphabet = string.ascii_lowercase
    sentence = sentenceCleaner(sentence)
    return set(sentence) == set(alphabet)

def sentenceCleaner(sentence):
    result = sentence.replace(" ", "").lower()
    return result