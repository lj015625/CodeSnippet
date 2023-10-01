cities = [
    {
        "name": "New York City",
        "country": "United States",
        "population": 20.14,
        "area": 1223.59
    },
    {
        "name": "Tokyo",
        "country": "Japan",
        "population": 37.47,
        "area": 2194.07,
    },
    {
        "name": "Los Angeles",
        "country": "United States",
        "population": 13.2,
        "area": 1299.01,
    },
    {
        "name": "Madrid",
        "country": "Spain",
        "population": 6.79,
        "area": 604.31,
    },
    {
        "name": "Osaka",
        "country": "Japan",
        "population": 19.3,
        "area": 5107.0,
    },
    {
        "name": "London",
        "country": "United Kingdom",
        "population": 14.26,
        "area": 8382.0,
    }
]

# Sort by population
cities = sorted(cities, key=lambda city: city['population'])

# Sort by population DESCENDING
cities = sorted(cities, key=lambda city: -city['population'])

# Sort by country, then by name
cities = sorted(cities, key=lambda city: (city['country'], city['name']))

# Sort by population density
cities = sorted(cities, key=lambda city: (city['population'] / city['area']))


movies = [
    (1994, 'The Shawshank Redemption', 9.2),
    (1999, 'Fight Club', 8.8),
    (1994, 'Pulp Fiction', 8.9),
    (1972, 'The Godfather', 9.2),
    (2008, 'The Dark Knight', 9.0)
]
#  sort our movies by rating, in descending order.
movies = sorted(movies, key=lambda movie: movie[2], reverse=True)
print(movies)
movies = sorted(movies, key=lambda movie: -movie[2])
print(movies)
