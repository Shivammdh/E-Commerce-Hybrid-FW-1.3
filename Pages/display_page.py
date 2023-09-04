class Display:
    ''' Displaying all the Value rating, price, people reviews etc'''
    def display_flipkart_data(self,product,flipkart_price,flipkart_rating,flipkart_people_rate,flipkart_review):
        print("Price for [{}] on all websites, Prices are in INR \n".format(product))
        print("Price available at Flipkart is: " + flipkart_price[1:])
        print("Total Rating at Flipkart is: " + flipkart_rating)
        print('Total people rating in flipkart:' + flipkart_people_rate)
        print('Total people review in flipkart:' + flipkart_review)

    def display_amazon_data(self,amazon_price,amazon_rating,amazon_pepol_rate,amazon_review):
        print("Price available at Amazon is: " + amazon_price)
        print("Total Rating at Amazon is: " + amazon_rating)
        print('Total people rating in Amazon:' + amazon_pepol_rate)
        print('Total people review in flipkart:' + amazon_review)

    def display_croma_data(self,corma_price,corma_rating,corma_pepole_rating,corma_pepole_review):
        print("Price available at Croma is: " + corma_price[1:])
        print("Total Rating at Croma is: " + corma_rating)
        print('Total people rating in corma:' + corma_pepole_rating)
        print('Total people review in corma:' + corma_pepole_review)