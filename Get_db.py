import Api_functions
import urllib.request
import time
import json


if __name__ == "__main__":
    apiKey=Api_functions.getApiKey()
    startMovie=int(input("Enter start movie id (by default 1):")or "1")
    numberOfMovie=int(input("Enter number of movies (by default 1000):")or "1000")
    setOfId=list(range(startMovie,numberOfMovie+startMovie))
    listOfMovies={}

    for i, movieId in enumerate(setOfId):
        try:
            print("Movie with id: {} is requested".format(movieId))
            result=Api_functions.getMovie(movieId, apiKey=apiKey)
        except urllib.request.HTTPError as error:
            if error.getcode() == 404:
                newMovieId=setOfId[-1]+1
                print("Movie with id: {} is not found and was changed by movie with id: {}".format(movieId, newMovieId))
                setOfId.append(newMovieId)
            elif error.getcode() == 429:
                pause = int(error.headers['X-RateLimit-Remaining'])
                print("Program has made to many requests. Wait {} seconds".format(pause + 1))
                time.sleep(pause + 1)
            continue
        movieTitle=result["title"]
        listOfMovies[movieTitle]=result
        print("Movie: {} was found. Movies to finish: {}".format(movieTitle, len(setOfId)-i-1))
    print("Collection of movies was successfully created")
    print("Exporting collection to moviesDataBase.json file")
    with open("moviesDataBase.json", 'w') as moviesDB:
        json.dump(listOfMovies, moviesDB)
    print("Movies Database was successfully created")



