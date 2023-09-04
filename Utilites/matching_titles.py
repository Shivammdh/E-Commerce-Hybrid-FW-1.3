from difflib import SequenceMatcher

def is_similar_enough(product_name1, product_name2, threshold=0.55):

    similarity_ratio = SequenceMatcher(None, product_name1, product_name2).ratio()
    # similarity_ratio1=similarity_ratio*100
    return similarity_ratio >= threshold
    # return similarity_ratio1

# # # # Example strings
# string1 = "APPLE iPhone 13 (Green, 128 GB)"
# s1=[s for s in string1 if s.isalpha() or s.isdigit()]
# cmp_s1="".join(s1).lower()
# print(s1)
# print(cmp_s1)
# string2 = ["Apple iPhone 13 (128GB) - Green",
#            "Apple iPhone 13 (128GB) - Starlight",
#            "Apple iPhone 14 (128 GB) - Starlight",
#            "Apple iPhone 13 (128GB) - Midnight",
#            "Apple iPhone 13 (128GB) - Blue",
#            "Apple iPhone 13 (128GB) - (Product) RED",
#            "Apple iPhone 13 (256GB) - Starlight",
#            "Apple iPhone 14 (128 GB) - Midnight",
#            "Apple iPhone 14 Plus (128 GB) - Starlight",
#            "Apple iPhone 13 (256GB) - Pink",
#            "Apple iPhone 13 (256GB) - Blue",
#            "Apple iPhone 13 (256GB) - (Product) RED",
#            "Apple iPhone 14 Plus (128 GB) - (Product) RED",
#            "Apple iPhone 14 (256 GB) - Starlight",
#            "Apple iPhone 14 (512 GB) - Starlight",
#            "Apple iPhone 14 Plus (256 GB) - Starlight"]
# list_of_items=[]
# for i in range(len(string2)):
# # # # Check if the strings are similar
#     s2=[s for s in string2[i] if s.isalpha() or s.isdigit()]
#     cmp_s2="".join(s2).lower()
#     # print(s2)
#     # print(cmp_s2)
#     # print(cmp_s2.lower())
#     result = is_similar_enough(s1, cmp_s2)
#     list_of_items.append((string2[i],result))
#
# print(list_of_items)
# # products_info = list(zip(prices, ratings, num_ratings, reviews))
#
# # Find the product with the lowest price
# higest_match_product = max(list_of_items, key=lambda x: x[1])
# print(higest_match_product)
#
# # sorted_items = sorted(li.items(), key=lambda x: x[1], reverse=True)
# # sorted_dict = {item[0]: item[1] for item in sorted_items}
# # print(list_of_dct)
#
#     # print(result)
# # if result:
# #     print("The strings are similar.")
# # else:
# #     print("The strings are not similar.")
