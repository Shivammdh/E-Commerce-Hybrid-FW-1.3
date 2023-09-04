def check_words_present(string1, string2):
    words1 = string1.split()
    words2 = string2.split()

    for word in words1:
        if word not in words2:
            return False

    return True

string1 = "APPLE iPhone 13 (Blue, 128 GB)"
string2 = "Apple iPhone 13 (128 GB) - Blue"

if check_words_present(string1, string2):
    print("All words in string1 are present in string2.")
else:
    print("Not all words in string1 are present in string2.")