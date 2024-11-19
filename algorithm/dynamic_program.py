# arguments are length of rod, and prices is a array indicate different length rod prices
def cut_rod(len, prices):
    max_value = 0
    if len == 0:
        return 0
    for i in range(1, len + 1):
        max_value = max(max_value, prices[i] + cut_rod(len-i, prices))
    return max_value


rod_prices = [0,1, 5, 8, 9 ,10, 17, 17, 20, 24, 30 ]
print(cut_rod(4, rod_prices))