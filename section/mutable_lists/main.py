# Initial travel wishlist with nested lists
travel_wishlist = [
    ["Paris", "France", 2000],
    ["Tokyo", "Japan", 3000],
    ["New York", "USA", 2500]
]

# Applying a 20% discount to the estimated cost
for trip in travel_wishlist:
    trip[2] *= 0.8

print("Updated list:", travel_wishlist)
# Printing the updated travel_wishlist to verify the change
print('Updated list:', travel_wishlist)