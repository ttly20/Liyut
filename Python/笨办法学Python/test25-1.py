import test25
sentence = "All good things come to those who wait."
words = test25.break_words(sentence)
print(""">>>import test25
>>>sentence = "All good things come to those who wait."
>>>words = test25.break_words(sentence)
>>>words""")
print(words)
sorted_words = test25.sort_words(words)
print(""">>>sorted_words = test25.sort_words(words)
>>>sorted_words""")
print(sorted_words)
test25.print_first_word(words)
test25.print_last_word(words)
print(""">>>test25.print_first_word(words)
>>>test25.print_last_word(words)
>>>words""")
print(words)
test25.print_first_word(sorted_words)
test25.print_last_word(sorted_words)
print(""">>>test25.print_first_word(sorted_words)
>>>test25.print_last_word(sorted_words)
>>>sorted_words""")
print(sorted_words)
sorted_words = test25.sort_sentence(sentence)
print(""">>>sorted_words = test25.sort_sentence(sentence)>>>sorted_words""")
print(sorted_words)
print(""">>>test25.print_first_and_last(sentence)""")
test25.print_first_and_last(sentence)
print(""">>>test25.print_first_and_last_sorted(sentence)""")
test25.print_first_and_last_sorted(sentence)
