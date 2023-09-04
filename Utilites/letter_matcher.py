def matching_percentage(string1, string2):
    # Calculate the length of the common letters between the two strings
    common_count = sum(1 for letter in string2 if letter in string1)

    # Calculate the percentage of common letters
    percentage = (common_count / len(string2)) * 100

    return percentage >= 70


string1 = ""
string2 = ""

if matching_percentage(string1, string2):
    print("At least 70% of the letters in the second string match the first string.")
else:
    print("Less than 70% of the letters in the second string match the first string.")
