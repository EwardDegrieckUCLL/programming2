from util import Card

def genres(movies):
    return {
        genre 
        for movie in movies
        for genre in movie.genres
    }
# first movies overlopen, want je moet eerst per film alle acteurs/genres overlopen. Je kan niet eerst de acteurs/genres overlopen zonder dat je weet over welke film het gaat

def actors(movies):
    return {
        actor
        for movie in movies
        for actor in movie.actors
    }
    
def repeat_consecutive(xs, n):
    return [
        x
        for x in xs
        for i in range(n)
    ]

# eerst zeggen welk element je iets mee wilt doen, en dan aantal keer herhalen. Je kan niet omgekeerd werken (logisch toch, cfr. eerste twee functies van deze oefening)

def repeat_alternating(xs, n):
    return [
        x
        for i in range(n)
        for x in xs
    ]

# nu eerst alle elementen van x, daarna pas herhalen (NIET mogelijk bij eerste twee functie, want daar heb je een attribuut nodig. Dus eerst instance benoemen vooraleer je attribuut kan opvragen)

def cards(values, suits):
    return {
        Card(value, suit)
        for value in values
        for suit in suits
    }