def movie_count(movies, director):
    return len([
        movie
        for movie in movies
        if movie.director == director
    ])

def longest_movie_runtime_with_actor(movies, actor):
    return max({
        movie.runtime 
        for movie in movies
        if actor in movie.actors
    })

def has_director_made_genre(movies, director, genre):
    return any({
            genre1 == genre
            for movie in movies
            for genre1 in movie.genres
            if movie.director == director
    })

def is_prime(n):
    return n > 1 and all([
        n % i != 0
        for i in range(2,n)
    ])

def is_increasing(ns):
    return all([
        ns[i] <= ns[i+1]
        for i in range(len(ns)-1)
    ])

def count_matching(xs, ys):
    return sum([
        int(xs[i] == ys[i])
        for i in range(min(len(xs), len(ys)))
    ])
# could also have used zip!

def weighted_sum(ns, weights):
    return sum([
        x * y
        for x, y
        in zip(ns, weights)
    ])

def alternating_caps(string):
    return ''.join([
        char.upper() if i % 2 == 0 else char.lower()
        for i, char in enumerate(string)
    ])

def find_repeated_words(sentence):
    import re
    words = [word.lower() for word in re.findall(r'[a-zA-Z]+', sentence)]
    return {word1 for word1, word2 in zip(words, words[1:]) if word1 == word2}