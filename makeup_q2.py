# Question 2

# Sample data to test with:

sample_budget = {'Facilities': 60000, 'Sales': 150000, 'Finance': 40000, 'R&D': 200000, 'Training': 25000}
sample_actual = {'R&D': 170000, 'Training': 25000, 'Finance': 38000, 'Sales': 162500, 'Facilities': 45000}


# Write your function below this line









# Test call -- do not change this
# Note that the order of the items in your returned dictionary does not matter.
# Depending on how you do the math, your last digit may differ.
print(unspent_pct(sample_budget, sample_actual))   # should print {'Facilities': 25.0, 'Finance': 5.0, 'R&D': 15.0}
