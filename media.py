import webbrowser


class Movie():
    """A representation of movie."""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer):
        """Constructor of the class Movie

        Args:
            title(str) : the movie title
            storyline(str) : the movie's storyline
            poster_image_url(str) : a url link to the box art image
            trailer_youtube_url(str): a url link to the trailer in youtube
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """Calling this function will open a web browser with the trail URL"""
        webbrowser.open(self.trailer_youtube_url)
