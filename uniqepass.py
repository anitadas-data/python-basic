def unique_words():
    para = input("Enter paragraph: ")

    words = set(para.split())

    new_word = input("Enter new word: ")
    words.add(new_word)

    remove_word = input("Enter word to remove: ")
    words.discard(remove_word)

    print("Random Removed:", words.pop())

    print("Unique Words:", words)
    print("Total Unique Words:", len(words))

unique_words()