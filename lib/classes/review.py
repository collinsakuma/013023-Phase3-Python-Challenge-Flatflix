class Review:
    
    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        Review.all.append(self)

    # rating property goes here!
    @property 
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if type(rating) == int and 1 <= rating <= 5:
            self._rating = rating
        else:
            raise Exception("rating is incorrect!")

    # viewer property goes here!
    @property 
    def viewer(self):
        return self._viewer

    @viewer.setter
    def viewer(self, viewer):
        from .viewer import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("not instance of Viewer class")

    # movie property goes here!
    @property 
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        from .movie import Movie
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception("not an instance of movie")