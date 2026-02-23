def total_calculations(amount, tip_prec):
    total = amount*(1+0.01*tip_prec)
    total = round(total, 2)
    print(f"please pay ${total}")
total_calculations(150,22)