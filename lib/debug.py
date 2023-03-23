#!/usr/bin/env python3
import ipdb
from classes.movie import Movie
from classes.review import Review
from classes.viewer import Viewer


if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
    movie_1 = Movie(title="Avatar: The Way of Water")
    Review(viewer=Viewer("Jeffrey"), movie=movie_1, rating=1)
    Review(viewer=Viewer("William"), movie=movie_1, rating=3)
    Review(viewer=Viewer("Benjamin"), movie=movie_1, rating=2)
    movie_2 = Movie(title="Scarface")
    Review(viewer=Viewer("Katherine"), movie=movie_2, rating=4)
    Review(viewer=Viewer("Catherine"), movie=movie_2, rating=5)
    movie_3 = Movie(title="Rashomon")
    Review(viewer=Viewer("Kathryn"), movie=movie_3, rating=5)
    Review(viewer=Viewer("Katrina"), movie=movie_3, rating=5)
    movie_4 = Movie(title="My Neighbor Totoro")
    Review(viewer=Viewer("Samwise"), movie=movie_4, rating=3)








# DO NOT REMOVE THIS
    ipdb.set_trace()
