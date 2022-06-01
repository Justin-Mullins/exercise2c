'''
Exercise 2c

Write a function that takes a list of words (strings). It should return a tuple con-
taining three integers, representing the length of the shortest word, the length
of the longest word, and the average word length.

'''

def compareLengths(*words):
    sum = 0
    shortest = 100
    longest = 0
    for word in words:
        sum += len(word)
        if (len(word) < shortest):
            shortest = len(word)
        elif (len(word) > longest):
            longest = len(word)
    average = sum / len(words)
    return (average, shortest, longest)

print(compareLengths(*['help', 'this', 'bed', 'rock', 'thunder']))
print(compareLengths(*('today', 'sand', 'ship', 'can', 'battle', 'break')))