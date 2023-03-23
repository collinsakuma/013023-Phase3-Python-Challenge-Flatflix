class Movie:
    
    all = []

    def __init__(self, title):
        self.title = title
        Movie.all.append(self)

    # title property goes here!
    @property 
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if type(title) == str and 0 < len(title):
            self._title = title
        else:
            raise Exception("title is incorect")

    @property 
    def reviews(self):
        from .review import Review
        review_list = []
        for review in Review.all:
            if review.movie == self:
                review_list.append(review)
        return review_list

    @property
    def reviewers(self):
        viewer_list = []
        for review in self.reviews:
            viewer_list.append(review.viewer)
        return viewer_list

    def average_rating(self):
        rating = 0
        for review in self.reviews:
            rating += review.rating
        return rating / len(self.reviews)

    @classmethod
    def highest_rated(cls):
        movies_obj = {}
        for movie in cls.all:
            movies_obj[movie] = movie.average_rating()

        return max(movies_obj, key = movies_obj.get)

