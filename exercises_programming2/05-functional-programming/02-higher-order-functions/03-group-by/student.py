def group_by(xs, key_function):
    return {
        key : [x for x in xs if key == key_function(x)]
        for key in {key_function(x) for x in xs}
    }

# deze oefening heb ik gemaakt zoals de year : list_of_movies_of_year cfr. vorig hoofdstuk