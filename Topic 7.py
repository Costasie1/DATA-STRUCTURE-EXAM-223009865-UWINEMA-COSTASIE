def counting_sort(arr, max_priority):

    count = [0] * (max_priority + 1)

    for city in arr:
        count[city['priority']] += 1

    for i in range(1, max_priority + 1):
        count[i] += count[i - 1]

    output = [None] * len(arr)

    for city in reversed(arr):
        output[count[city['priority']] - 1] = city
        count[city['priority']] -= 1
    
    return output
cities = [
    {'name': 'City A', 'priority': 3},
    {'name': 'City B', 'priority': 1},
    {'name': 'City C', 'priority': 2},
    {'name': 'City D', 'priority': 4},
    {'name': 'City E', 'priority': 1}
]

# Maximum priority value in the data
max_priority = 4

# Sort the data based on priority
sorted_cities = counting_sort(cities, max_priority)

# Print the sorted data
for city in sorted_cities:
    print(f"City: {city['name']}, Priority: {city['priority']}")
