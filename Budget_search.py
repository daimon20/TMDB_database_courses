import Api_functions
import urllib.request

if __name__ == "__main__":
    movieId = int(input("Enter movie_id"))

    try:
        movie = Api_functions.getMovie(movieId)
    except urllib.request.HTTPError as error:
        if error.getcode() == 404:
            print("Can't find the movie with ID {}".format(movieId))
            exit(1)
        else:
            print(error.msg)
            exit(1)
    print("Budget of Movie: {} is {}".format((movie["title"], movie["budget"])))
