movies = [
    {
        "title": "Ghilli",
        "year": 2004,
        "genres": ["Comedy", "Romance", "Action", "War"],
        "primary_audio": "Tamil",
        "dubbed_languages": [
            "Spanish",
            "French",
            "German",
            "Italian",
            "Tamil",
            "Russian",
        ],
        "parental_rating": "PG-13",
    },
    {
        "title": "Charlie",
        "year": 2015,
        "genres": ["Action", "Thriller", "Drama", "War", "Epic"],
        "primary_audio": "Malayalam",
        "dubbed_languages": [
            "Spanish",
            "French",
            "German",
            "Malayalam",
            "Tamil",
            "Russian",
        ],
        "parental_rating": "R",
    },
    {
        "title": "CIA",
        "year": 2017,
        "genres": ["Action", "Thriller", "Crime"],
        "primary_audio": "Malayalam",
        "dubbed_languages": [
            "Spanish",
            "French",
            "German",
            "Italian",
            "Malayalam",
        ],
        "parental_rating": "R",
    },
    {
        "title": "Sarkar",
        "year": 2018,
        "genres": ["Action", "Thriller", "Crime", "Sci-fi"],
        "primary_audio": "Tamil",
        "dubbed_languages": [
            "Spanish",
            "French",
            "German",
            "Tamil",
            "Italian",
            "Russian",
        ],
        "parental_rating": "R",
    },
]


def get_filtered_movies(movies, genre, audio):
    genre = genre.lower()
    audio = audio.lower()

    filtered_movies = []
    for movie in movies:
        if genre in [g.lower() for g in movie["genres"]] and audio in [
            a.lower() for a in movie["dubbed_languages"]
        ]:
            filtered_movies.append(movie)
    return filtered_movies


def print_movies(movies):
    if not movies:
        print("No movies found matching your criteria.")
        return

    for ind, movie in enumerate(movies, start=1):
        print(f"Movie #{ind}")
        print(f"Title: {movie['title']}")
        print(f"Year: {movie['year']}")
        print(f"Genres: {', '.join(movie['genres'])}")
        print(f"Parental Rating: {movie['parental_rating']}")
        print()


genre = input("Enter the genre: ").strip()
audio = input("Enter your preferred audio language: ").strip()

filtered_movies = get_filtered_movies(movies, genre, audio)
print_movies(filtered_movies)