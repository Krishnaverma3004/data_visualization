age = int(input("Enter patient age: "))
heart_rate = int(input("Enter heart rate (bpm): "))
severe_injury = input("Severe injury? (yes/no): ")
condition = "Normal"

# Categorize patient
if heart_rate < 60 or heart_rate > 100 or severe_injury == "yes":
    condition = "Critical"
elif heart_rate >= 60 and heart_rate <= 100 and severe_injury == "no":
    condition = "Moderate"

# Upgrade priority if age > 65
if age > 65 and condition == "Moderate":
    condition = "Critical"

print("Patient priority:", condition)

