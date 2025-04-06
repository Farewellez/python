gas =[4,5,7,4]
cost= [6, 6, 3, 5]

maximum = float("-Inf")
for i in range(len(gas)):
    # Membuat selisih
    difference = gas[i] - cost[i]
    # Mencari selisih paling kecil
    print(f"{difference} apakah > {maximum}?",end=" ")
    print(difference > maximum)
    if difference > maximum:
        maximum = difference
    print("Ini maximum baru:",maximum)