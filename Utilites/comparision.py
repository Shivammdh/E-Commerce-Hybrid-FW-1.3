def compare_products(prices, ratings, num_ratings,reviews):
    # Combine the product information into a list of tuples
    products_info = list(zip(prices, ratings, num_ratings,reviews))
    
    # Find the product with the lowest price
    lowest_price_product = min(products_info, key=lambda x: x[0])

    # Find the product with the highest rating
    highest_rating_product = max(products_info, key=lambda x: x[1])

    # Find the product with the highest number of ratings
    highest_num_ratings_product = max(products_info, key=lambda x: x[2])

    highest_num_reviews = max(products_info, key=lambda x: x[3])
    return lowest_price_product, highest_rating_product, highest_num_ratings_product, highest_num_reviews

# # Example data for the products
# prices = [61900, 61534, 61999]
# ratings = [4.5, 4.4, 4.9]
# num_ratings = [612, 515, 20]

#
# # Call the function to get the comparison result
# lowest_price_product, highest_rating_product, highest_num_ratings_product = compare_products(prices, ratings, num_ratings)
#
# # Output the result
# print("Product with Lowest Price:")
# print(f"Price: {lowest_price_product[0]}, Rating: {lowest_price_product[1]}, Number of Ratings: {lowest_price_product[2]}")
#
# print("\nProduct with Highest Rating:")
# print(f"Price: {highest_rating_product[0]}, Rating: {highest_rating_product[1]}, Number of Ratings: {highest_rating_product[2]}")
#
# print("\nProduct with Highest Number of Ratings:")
# print(f"Price: {highest_num_ratings_product[0]}, Rating: {highest_num_ratings_product[1]}, Number of Ratings: {highest_num_ratings_product[2]}")
