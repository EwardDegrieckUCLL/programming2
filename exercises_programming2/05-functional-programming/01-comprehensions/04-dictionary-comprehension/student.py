def title_to_director(movies):
    return {
        movie.title : movie.director
        for movie
        in movies
    }

def director_to_titles(movies):
    def get_all_directors_set(movies_list):
        return {
            movie.director
            for movie
            in movies_list
        }

    def list_of_movie_titles_of_director(director, movies_list):
        return [
            movie.title
            for movie
            in movies_list
            if movie.director == director
        ]
    
    return {
        director: list_of_movie_titles_of_director(director, movies)
        for director
        in get_all_directors_set(movies)
    }

    # i got this exercise right! allthough i wasted some coding space by using diff functions instead of making code more compact