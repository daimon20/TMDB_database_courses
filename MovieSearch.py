import Json_functions

if __name__ == "__main__":
    filePath = input("Enter relative path to your movie database (by default moviesDataBase.json)") or "moviesDataBase.json"
    file=Json_functions.readJson(filePath)
    indexes=frozenset(file.keys())
    print("Now program is ready to find a film for you")
    request=input("What do you want to find").lower()
    result=[name for name in indexes if request in name.lower()]
    if not result:
        print("There are no films for your request")
    else:
        print(sorted(result))



