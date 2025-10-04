while True:              #this file is capable of giving you as many jokes as you want in one run
    import requests
    url="https://official-joke-api.appspot.com/random_joke"
    response=requests.get(url)
    joke=response.json()
    print(joke["setup"])
    input()

    print(joke["punchline"])
