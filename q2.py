# Question 2

# Sample data to test with:

sample_budget = {'Marketing': 50000, 'IT': 120000, 'HR': 30000, 'Operations': 85000, 'Legal': 40000}
sample_actual = {'IT': 131500, 'Legal': 38250, 'Marketing': 50000, 'Operations': 91200.75, 'HR': 29100}


# Write your function below this line









# Test call -- do not change this
# Note that the order of the items in your returned dictionary does not matter.
print(over_budget(sample_budget, sample_actual))   # should print {'IT': 11500, 'Operations': 6200.75}
