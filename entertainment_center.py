import media
import fresh_tomatoes


# Storyline and poster taken from respective IMDB page

# Create an instance of movie
avengers = media.Movie(
    "The Avengers",  # Movie Title

    "Earth's mightiest heroes must come together and learn to fight as a team "
    "if they are going to stop the mischievous Loki "
    "and his alien army from enslaving humanity.",  # Movie Storyline

    "https://ia.media-imdb.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA  # Box Art Image

    "https://www.youtube.com/watch?v=eOrNdBpGMv8"  # NOQA  # Trailer
    )

# Create an instance of movie
spiderman = media.Movie(
    "Spider-Man: Homecoming",  # Movie Title

    "Peter Parker balances his life as an ordinary high school student "
    "in Queens with his superhero alter-ego Spider-Man,"
    " and finds himself on the trail of a new menace "
    "prowling the skies of New York City.",  # Movie Storyline

    "https://ia.media-imdb.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_SY1000_CR0,0,658,1000_AL_.jpg",  # NOQA  # Box Art Image

    "https://www.youtube.com/watch?v=lCkVr1n1eCA"  # NOQA  # Trailer
    )

# Put the two instances into an array
movie = [avengers, spiderman]

# Call the method in fresh_tomatoes.py to create the website.
fresh_tomatoes.open_movies_page(movie)
