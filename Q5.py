oxygen_levels = []

def is_valid_oxygen_level(value):
    return 1 <= value <= 100

for round_num in range(1, 4):
    for trainee_num in range(1, 4):
        try:
            oxygen_value = int(input(f"Round {round_num}\nOxygen value of trainee {trainee_num}: "))
            if not is_valid_oxygen_level(oxygen_value):
                print("INVALID INPUT")
            oxygen_levels.append(oxygen_value)
        except ValueError:
            print("INVALID INPUT")

averages = []
for i in range(3):
    avg = round(sum(oxygen_levels[i::3]) / 3)
    averages.append(avg)

highest_avg = max(averages)
    
if highest_avg < 70:
    print("INVALID INPUT")
else:
    most_fit_trainees = [i + 1 for i, avg in enumerate(averages) if avg == highest_avg]
    for trainee in most_fit_trainees:
        print(f"Trainee Number : {trainee}")
    print(f"Highest Average Oxygen Level : {highest_avg}")
