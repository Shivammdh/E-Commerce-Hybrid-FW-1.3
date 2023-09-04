def find_avrage(five_star,one_star):
    lst_avg=[five_star,one_star]
    final_avg = []
    for vp in lst_avg:
        if ',' in vp:
            val = vp.replace(',', '')
            final_avg.append(int(val))
        else:
            final_avg.append(int(vp))
    # total_peoples_rating = [f_rate, a_rate, c_rate]

    total_ratings = final_avg[0] + final_avg[1]
    average_five_star = (final_avg[0] / total_ratings) * 100
    average_one_star = (final_avg[1] / total_ratings) * 100
    return average_five_star,average_one_star
    # Print the results
    # print(f"Average 5-star ratings: {average_five_star:.2f}%")
    # print(f"Average 1-star ratings: {average_one_star:.2f}%")
