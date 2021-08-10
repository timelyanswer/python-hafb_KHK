#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/10/2021
Purpose: review the filter() function, functools
"""
from functools import reduce
import operator



def count_words(doc):
    """count words in a document
    produces a dictionary of mapping words"""
    # first step normalize the string

    normalize_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalize_doc.split():
        frequencies[word] = frequencies.get(word, 0) +1
    return frequencies

def combine_counts(d1, d2):
    """combine two word dictionaries"""
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d









# --------------------------------------------------
def main():
    """Make your noise here"""

    numbers = [-55, 2, 4, -5, 4, 5, 2, 90, 80]
    # task: create a list of all positive numbers

    # list comprehension
    positives = [num for num in numbers if num >= 0]
    print(positives)

    # generator
    positives = list((num for num in numbers if num >= 0))
    print(positives)

    # filter() and lambda
    #filter is also a lazy evaluation
    positives = list(filter(lambda x: x > 0, numbers))
    print(positives)

    # a+b = operator.add(a,b)
    accumulator = operator.add(positives[0], positives[1])
    for item in numbers[2:]:
        accumulator = operator.add(accumulator, item)
    print(accumulator)

    numbers = []
    print(reduce(operator.add, numbers, 0))

    document = 'this is going to be the test situation'
    print(count_words(document))

    documents = [
        'it was the best of titmes, it was the worst of times',
        'i went ot the home of the old person',
        'there was not any way to help them'
    ]

    counts = map(count_words, documents)
    total_counts = reduce(combine_counts, counts)
    print(total_counts)














# --------------------------------------------------

