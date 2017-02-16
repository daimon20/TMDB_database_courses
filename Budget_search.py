import Api_functions
import urllib.request

if __name__ == "__main__":
    movie_id = int(input("Enter movie_id"))

    try:
        movie = Api_functions.find_movie(movie_id)
    except urllib.request.HTTPError as error:
        if error.getcode() == 404:
            print("Can't find the movie with ID {}".format(movie_id))
            exit(1)
        else:
            print(error.msg)
            exit(1)
    print("Budget of Movie: {} is {}".format((movie["title"], movie["budget"])))
