import difflib


def suggest_correct_word(word, word_list):
    new_word_list=[item[0] for item in [p for p in word_list]]
    print(new_word_list)
    closest_match = difflib.get_close_matches(word, word_list)


    if closest_match:
        return closest_match[0]
    else:
        return "No suggestions available"


# # List of example words
# word_list=['OnePlus 11 5G 128GB','One Pluse CE2 5G', 'OnePluse 11R 5G Titen Black 256GB', 'OnePlus 11 5G 256GB']
# # #
# # # # Get user input
# # # # user_input = input("Enter a word: ")
# user_input = "OnePlus 11 5G"
# # #
# # # # Find the closest match and suggest it
# suggested_word = suggest_correct_word(user_input, word_list)
# print("Suggested word:", suggested_word)
