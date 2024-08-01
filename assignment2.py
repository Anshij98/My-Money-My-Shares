def distribute_apples():
    # Define the amount paid by each person
    ram_paid = 50
    sham_paid = 30
    rahim_paid = 20

    # Initialize lists to store apple weights for each person
    ram_apples = []
    sham_apples = []
    rahim_apples = []

    # Initialize total weights for each person
    ram_total = 0
    sham_total = 0
    rahim_total = 0

    # Initialize expected total weights for each person
    total_weight = 0

    # Get apple weights from user
    apple_weights = []
    while True:
        weight = int(input("Enter apple weight in grams (-1 to stop): "))
        if weight == -1:
            break
        apple_weights.append(weight)
        total_weight += weight

    # Calculate the proportion of total weight for each person
    ram_expected = (ram_paid / (ram_paid + sham_paid + rahim_paid)) * total_weight
    sham_expected = (sham_paid / (ram_paid + sham_paid + rahim_paid)) * total_weight
    rahim_expected = (rahim_paid / (ram_paid + sham_paid + rahim_paid)) * total_weight

    # Sort apple weights in descending order
    apple_weights.sort(reverse=True)

    # Distribute apples among Ram, Sham, and Rahim
    for weight in apple_weights:
        # Determine who needs more apples based on their expected weight
        if ram_total < ram_expected:
            ram_apples.append(weight)
            ram_total += weight
        elif sham_total < sham_expected:
            sham_apples.append(weight)
            sham_total += weight
        elif rahim_total < rahim_expected:
            rahim_apples.append(weight)
            rahim_total += weight

    # Print the distribution result
    print("Distribution Result:")
    print("Ram:", ", ".join(map(str, ram_apples)))
    print("Sham:", ", ".join(map(str, sham_apples)))
    print("Rahim:", ", ".join(map(str, rahim_apples)))

# Run the program
distribute_apples()
