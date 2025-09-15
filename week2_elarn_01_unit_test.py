def calculate_discount(loyalty_points):
    if loyalty_points >= 1000:
        return 20
    elif loyalty_points >= 500:
        return 10
    else:
        return 0