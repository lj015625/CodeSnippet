"""Given a list of tuples featuring names and grades on a test,
write a function normalize_grades to normalize the values of the grades to a linear scale between 0 and 1."""
import numpy as np

def normalize_grades(tuples):
    low_value = min(x[1] for x in tuples)
    high_value = max(x[1] for x in tuples)
    return [(x[0], (x[1]-low_value)/(high_value-low_value)) for x in tuples]

def z_normalize_grades(tuples):
    values = [x[1] for x in tuples]
    mean = sum(values) / len(values)
    differences = [(value - mean)**2 for value in values]
    sum_of_differences = sum(differences)
    standard_deviation = (sum_of_differences / (len(values) - 1)) ** 0.5
    # standard_deviation = np.std([values], ddof=1)
    return [(x[0], (x[1]-mean)/standard_deviation) for x in tuples]


tuples = [
    ('Jason', 94),
    ('Tessa', 80),
    ('Carla', 38),
    ('Matt', 43),
    ('Jessica', 100)
]
print(normalize_grades(tuples))
print(z_normalize_grades(tuples))

