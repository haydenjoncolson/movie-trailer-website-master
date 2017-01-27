#import fresh_tomatoes
import fresh_tomatoes
import media

# Data Model
# Each movies contains a title, quote, poster image, and youtube trailer.

the_interview = media.Movie("The Interview",
"James Franco and Seth Rogen go to North Korea. ",
"http://www.impawards.com/2014/posters/interview.jpg",
"https://www.youtube.com/watch?v=OHC2JDsJWes")

pineapple_express = media.Movie("Pineapple Express",
"James Franco and Seth Rogen become brothers"
" through a series of crazy events. ",
"https://upload.wikimedia.org/wikipedia/en/c/ca/"
"Pineapple_Express_Poster.jpg",
"https://www.youtube.com/watch?v=BWZt4v6b1hI")

this_is_the_end = media.Movie("This Is The End",
"James Franco, Seth Rogen, and friends face the end of the world. ",
"https://upload.wikimedia.org/wikipedia/en/3/36/"
"This-is-the-End-Film-Poster.jpg",
"https://www.youtube.com/watch?v=Yma-g4gTwlE")

the_godfather = media.Movie("The Godfather",
"The life of the Corleone Family.",
"https://i.ytimg.com/vi/rt-r-w7Z2Ag/maxresdefault.jpg",
"https://www.youtube.com/watch?v=sY1S34973zA")

goodfellas = media.Movie("Goodfellas",
"As far back as I remember, I wanted to be a gangster.",
"http://static.srcdn.com/slir/w570-h379-q90-c570:379/wp-content/uploads/"
"Goodfellas-TV-show-Martin-Scorsese.jpg",
"https://www.youtube.com/watch?v=qo5jJpHtI1Y")

casino = media.Movie("Casino",
"Robert De Niro runs a Las Vegas casino for the mob.",
"http://www.assopoker.com/wp-content/uploads/2011/03/casino-movie.jpg",
"https://www.youtube.com/watch?v=j-D0QiMpGKc")


# Array of movies

movies = [the_interview, pineapple_express, this_is_the_end,
          the_godfather, goodfellas, casino]

# Run the open movies page function from the fresh tomatoes file

fresh_tomatoes.open_movies_page(movies)
