# list of movies and showing the list 
my_fav_movies = ['Iron Man', 'Captain America', 'The Avengers']
print(f"The list my_fav_movies includes my top {len(my_fav_movies)} movies.")
print(my_fav_movies)
 
# now we're focusing on sorting
print(sorted(my_fav_movies))
print(my_fav_movies) # first code changes the order, second brings back to normal 

# using a different method to sort
my_fav_movies.sort()
print(my_fav_movies) # this output only provides one list

# added another movie

my_fav_movies.append('Spider-Man')
print(f"The updated list of my_fav_movies includes my top {len(my_fav_movies)} favorite movies.")
print(my_fav_movies)

