import matplotlib.pyplot as plt

with open("sequence.txt", "r") as file:
    sequence = [float(line.strip()) for line in file]

# Option 1: Number of numbers less than and greater than 0
less_than_zero = len([num for num in sequence if num < 0])
greater_than_zero = len([num for num in sequence if num > 0])
percentages_1 = [less_than_zero / len(sequence) * 100, greater_than_zero / len(sequence) * 100]

# Option 2: Sum modulo the first 125 numbers and the second 125 numbers
sum_first_125 = sum(sequence[:125])
sum_second_125 = sum(sequence[125:])
percentages_2 = [abs(sum_first_125) / (abs(sum_first_125) + abs(sum_second_125)) * 100,
                 abs(sum_second_125) / (abs(sum_first_125) + abs(sum_second_125)) * 100]

# Option 3: The modulo sum of numbers in even and odd positions
even_sum = sum(sequence[::2])
odd_sum = sum(sequence[1::2])
percentages_3 = [abs(even_sum) / (abs(even_sum) + abs(odd_sum)) * 100,
                 abs(odd_sum) / (abs(even_sum) + abs(odd_sum)) * 100]

# Option 4: Average modulo of the first 125 and second 125 numbers
avg_first_125 = sum(sequence[:125]) / len(sequence[:125])
avg_second_125 = sum(sequence[125:]) / len(sequence[125:])
percentages_4 = [abs(avg_first_125) / (abs(avg_first_125) + abs(avg_second_125)) * 100,
                 abs(avg_second_125) / (abs(avg_first_125) + abs(avg_second_125)) * 100]

# Option 5: Average modulo of numbers in even and odd positions
avg_even = sum(sequence[::2]) / (len(sequence) // 2)
avg_odd = sum(sequence[1::2]) / (len(sequence) - (len(sequence) // 2))
percentages_5 = [abs(avg_even) / (abs(avg_even) + abs(avg_odd)) * 100,
                 abs(avg_odd) / (abs(avg_even) + abs(avg_odd)) * 100]

# Option 6: Numbers greater than 5 and less than 5, discard negative ones
greater_than_5 = len([num for num in sequence if num > 5])
less_than_minus_5 = len([num for num in sequence if num < -5])
percentages_6 = [greater_than_5 / len(sequence) * 100, less_than_minus_5 / len(sequence) * 100]

# Option 7: Numbers greater than -5 and less than -5, discard positive ones
greater_than_minus_5 = len([num for num in sequence if num > -5])
less_than_5 = len([num for num in sequence if num < 5])
percentages_7 = [greater_than_minus_5 / len(sequence) * 100, less_than_5 / len(sequence) * 100]

# Option 8: Numbers from 0 to 5 and numbers from 0 to -5, discard the rest
between_0_and_5 = len([num for num in sequence if 0 <= num <= 5])
between_0_and_minus_5 = len([num for num in sequence if 0 >= num >= -5])
percentages_8 = [between_0_and_5 / len(sequence) * 100, between_0_and_minus_5 / len(sequence) * 100]

# Option 9: Numbers from 5 to 10 and numbers from -5 to -10, discard the rest
between_5_and_10 = len([num for num in sequence if 5 <= num <= 10])
between_minus_5_and_minus_10 = len([num for num in sequence if -5 >= num >= -10])
percentages_9 = [between_5_and_10 / len(sequence) * 100, between_minus_5_and_minus_10 / len(sequence) * 100]

# Option 10: Numbers from -3 to 3 and others
between_minus_3_and_3 = len([num for num in sequence if -3 <= num <= 3])
others = len(sequence) - between_minus_3_and_3
percentages_10 = [between_minus_3_and_3 / len(sequence) * 100, others / len(sequence) * 100]

# Plotting the percentage chart for each option on a page
options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentages = [percentages_1, percentages_2, percentages_3, percentages_4, percentages_5,
               percentages_6, percentages_7, percentages_8, percentages_9, percentages_10]


labels = ["Less than 0 vs Greater than 0", "Sum modulo first 125 vs second 125",
          "Modulo sum of even vs odd positions", "Average modulo first 125 vs second 125",
          "Average modulo of even vs odd positions", "Greater than 5 vs Less than -5 (discard negative)",
          "Greater than -5 vs Less than 5 (discard positive)",
          "Between 0 and 5 vs Between 0 and -5 (discard the rest)",
          "Between 5 and 10 vs Between -5 and -10 (discard the rest)",
          "Between -3 and 3 vs Others"]

fig, axes = plt.subplots(5, 2, figsize=(12, 18))

for i, option in enumerate(options):
    row = i // 2
    col = i % 2
    bars = axes[row, col].bar(["Option", "Others"], percentages[i])
    axes[row, col].set_ylabel("Percentage")

    for bar in bars:
        yval = bar.get_height()
        axes[row, col].text(bar.get_x() + bar.get_width() / 2, yval, f"{yval:.2f}%", ha='center', va='bottom')

    axes[row, col].set_title(labels[i], pad=20)  # Adjusting the position of the title

plt.subplots_adjust(hspace=1, wspace=0.2)  # Adjusting the spacing between subplots
plt.show()
