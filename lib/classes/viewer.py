class Viewer:
    
    all_usernames = []
    all = []

    def __init__(self, username):
        self.username = username
        Viewer.all_usernames.append(self.username)
        Viewer.all.append(self)

    # username property goes here!
    @property 
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if type(username) == str and 6 <= len(username) <= 16 and username not in Viewer.all_usernames:
            self._username = username
        else:
            raise Exception('user name incorrect')

    @property
    def reviews(self):
        from .review import Review
        review_list = []
        for review in Review.all:
            if review.viewer == self:
                review_list.append(review)
        return review_list

    @property
    def reviewed_movies(self):
        movie_list = []
        for review in self.reviews:
            movie_list.append(review.movie)
        return movie_list

    def reviewed_movie(self, movie):
        return movie in self.reviewed_movies

    def rate_movie(self, movie, rating):
        from .review import Review
        if (movie in self.reviewed_movies):
            for review in self.reviews:
                if(review.movie == movie):
                    review._rating = rating
        else:
            Review(self, movie, rating)


