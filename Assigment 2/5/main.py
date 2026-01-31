def price():
    while True:
        diameter1 = float(input("diameter of a first round pizza (cm): "))
        pizza_price1 = float(input("price of first pizza (USD): "))
        area1 = (diameter1/2)**2 * 3.14
        total_cost1 = pizza_price1/area1
        
        diameter2 = float(input("diameter of a first round pizza (cm): "))
        pizza_price2 = float(input("price of first pizza (USD): "))
        area2 = (diameter2/2)**2 * 3.14
        total_cost2 = pizza_price2/area2
        
        if (total_cost1 > total_cost2):
            total_cost1 = '1'
        else:
            total_cost1 = '2'
        print(f'The better value for money is pizza {total_cost1}')
price()