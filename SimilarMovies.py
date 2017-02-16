import Json_functions
import Api_functions

if __name__ == "__main__":
    filePath = input("Enter relative path to your movie database (by default moviesDataBase.json)") or "moviesDataBase.json"
    file=Json_functions.readJson(filePath)
    print("Now program is ready to find similar films for you")
    favMovie=input("Enter your favourite film:")
    if favMovie not in file:
        print("Program can't find this movie in DB. Restart and try another film")
    else:
        movie = file[favMovie]
        listOfSimilar = list()
        for title in file:
            if title == favMovie:
                continue
            indexOfSimilarity = Api_functions.getIndexOfFilmsSimmilarity(file[title], movie)
            listOfSimilar.append({"title": title, "index": indexOfSimilarity})
        listOfSimilar.sort(key=lambda i: i['index'], reverse=True)
        print("This 10 films a the most similar to your favourite")
        print("\n".join(["{}. {}" .format(index + 1, movie["title"])
                         for index, movie in enumerate(listOfSimilar[:10])]))

