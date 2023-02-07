import requests as re

token = "GQVJVN0FqZAzFHOHlEbUJsNkhJVXNERURwZAWhvU3Mtd29SeTl0LVJheDBqRVNydVdEWF9uNzQ5NkZAOeU5rRVJDdk82bWljWUhfdUkxdU1KUzVNTGlzSFNjZA0NJVVVIWE5vV0wwd21DVVNad0VITVRWa0hsS0NqbS0zX3VF"
fields = "id,caption"


url = f"https://graph.instagram.com/me/media?fields={fields}&access_token={token}"

r = re.get(url)

print(r.text)