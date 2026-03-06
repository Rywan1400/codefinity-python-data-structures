space_movies = ('2001: A Space Odyssey', 'Interstellar', 'Star Wars: Episode IV - A New Hope', 'Gravity', 'The Martian')

new_movies = ['The Lion King', 'Jurassic Park', 'Finding Nemo']

# Write your code here

# 1. Convert list to tuple
animal_movies = tuple(new_movies) 
# 2. Concatenate tuples
movie_poster = animal_movies + space_movies

# Testing
print("Now playing in theaters:", movie_poster)