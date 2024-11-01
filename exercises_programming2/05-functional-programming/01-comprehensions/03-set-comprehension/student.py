def directors(movies):
    return {
        movie.director
        for movie
        in movies
    }

def common_elements(xs, ys):
    return {
        el
        for el
        in xs
        if el in ys
    }