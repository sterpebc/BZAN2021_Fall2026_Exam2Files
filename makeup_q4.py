# Question 4

# The sample file mileage.csv is in the same folder as this file.

# Sample data to test with:

sample_routes = {
    'North Loop': ['Cleveland', 'Akron', 'Columbus'],
    'West Run':   ['Toledo', 'Dayton', 'Cincinnati'],
    'Southbound': ['Cincinnati', 'Columbus', 'Akron'],
    'Lakeshore':  ['Akron', 'Cleveland', 'Toledo'],
    'Shortcut':   ['Cleveland', 'Columbus', 'Cincinnati'],
    'Crosstown':  ['Toledo', 'Akron', 'Dayton', 'Cincinnati'],
}


# Write your function below this line









# Test call -- do not change this
# Note that the order of the tuples in your returned list does not matter.
print(missing_roads('mileage.csv', sample_routes))   # should print [('Shortcut', 1), ('Crosstown', 2)]
