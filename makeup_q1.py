# Question 1

# Sample data to test with:

sample_inventory = {'Paper towels': 18, 'Coffee pods': 60, 'Napkins': 45, 'Cups': 120, 'Sugar packets': 45}


# Write your function below this line









# Test calls -- do not change these
# Note that the order of the names in your returned list does not matter.
print(overstocked(sample_inventory, 45))    # should print ['Coffee pods', 'Cups']
print(overstocked(sample_inventory, 100))   # should print ['Cups']
