patient = ("John Doe", 45, 120, 80)
print("Patient tuple:", patient)

print("\nAge:", patient[1])
print("Heart Rate:", patient[3])

print("\nTuples are immutable; patient vitals cannot be changed accidentally.")

patient_list = list(patient)
patient_list[3] = 85
patient = tuple(patient_list)
print("\nUpdated patient tuple:", patient)

patients = (
    ("John Doe", 45, 120, 80),
    ("Mary Ann", 30, 110, 75),
    ("Ali Omar", 50, 130, 78),
    ("Grace Kim", 28, 118, 72),
    ("Peter Lee", 60, 140, 82)
)

names = [p[0] for p in patients]
print("\nPatient names:", names)
