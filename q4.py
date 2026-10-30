# Question 4

# The sample file distances.csv is in the same folder as this file.

# Sample data to test with:

sample_routes = {
    'Route A': ['Boston', 'Worcester', 'Springfield', 'Hartford', 'New Haven'],
    'Route B': ['Boston', 'Providence', 'New Haven'],
    'Route C': ['New Haven', 'Hartford', 'Worcester', 'Boston'],
    'Route D': ['Boston', 'Providence', 'Hartford', 'Springfield'],
    'Route E': ['Boston', 'Hartford', 'New Haven'],
}


# Write your function below this line









# Test call -- do not change this
# Note that the order of the tuples in your returned list does not matter.
print(route_lengths('distances.csv', sample_routes))   # should print [('Route A', 165.5), ('Route B', 155.0), ('Route C', 153.0), ('Route D', 162.5)]
