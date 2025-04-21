import random
import json

def load_movies():
    with open("movies.json", "r", encoding="utf-8") as file:
        return json.load(file)

def recommend_movie(genre):
    movies = load_movies()
    filtered = [m for m in movies if genre.lower() in m["genre"].lower()]
    return random.choice(filtered) if filtered else None

if __name__ == "__main__":
    genre = input("Введите жанр: ")
    movie = recommend_movie(genre)
    if movie:
        print(f"🎬 Советую фильм: {movie['title']} — {movie['description']}")
    else:
        print("Фильмы не найдены.")

