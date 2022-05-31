# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 5/30/2022
# Description: Collection of classes that creates Movie and StreamingService objects and returns whether a Movie is on
#   a StreamingService.

class Movie:
    """Represents a Movie with a title, genre, director, and release year."""

    def __init__(self, title, genre, director, year):
        """Creates a Movie object with a title, genre, director, and release year."""
        self._title = title
        self._genre = genre
        self._director = director
        self._year = int(year)

    def get_title(self):
        """Returns the movie's title."""
        return self._title

    def get_genre(self):
        """Returns the movie's genre."""
        return self._genre

    def get_director(self):
        """Returns the movie's director."""
        return self._director

    def get_year(self):
        """Returns the movie's release year."""
        return self._year


class StreamingService:
    """Represents a Streaming Service with its name nad Movie catalog."""

    def __init__(self, name):
        """Creates a StreamingService object with a name and catalog."""
        self._name = name
        self._catalog = {}

    def get_name(self):
        """Returns the name."""
        return self._name

    def get_catalog(self):
        """Returns the catalog."""
        return self._catalog

    def add_movie(self, Movie):
        """Adds a movie to the catalog."""

        self._catalog[Movie.get_title()] = Movie

    def delete_movie(self, title):
        """Removes Movie with given title from the catalog."""

        del self._catalog[title]


class StreamingGuide:
    """Represents a guide to which Streaming Service has a given movie."""

    def __init__(self):
        """Creates an empty list."""

        self._Guide = []

    def add_streaming_service(self, StreamingService):
        """Adds a StreamingService object to the list."""

        self._Guide.append(StreamingService)

    def delete_streaming_service(self, name):
        """Removes a StreamingService object from the list."""

        for service in self._Guide:

            if service.get_name() == name:

                self._Guide.remove(service)

                return

    def where_to_watch(self, title):
        """Returns a list of Streaming Services showing a Movie given a title."""

        returnvalue = None

        for service in self._Guide:

            if title in service.get_catalog():

                movie = service.get_catalog()[title]

                if returnvalue is None:

                    returnvalue = [movie.get_title() + " (" + str(movie.get_year()) + ")"]

                returnvalue.append(service.get_name())

        return returnvalue