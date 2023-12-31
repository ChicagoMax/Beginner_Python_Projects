def replace_word():

    str = "Hi guys, my favorite team this week is the Bulls"
    print(str)
    word_to_replace = input("Which word would you like to replace? ")
    word = input('Which word would you like to replace it with? ')
    print(str.replace(word_to_replace,word))

replace_word()