import fresh_tomatoes
import media

# Create multiple instances of Movie with favorite movie information

toy_story = media.Movie('The Matrix',
                        'A computer hackers learns about his true reality.',
                        'http://goo.gl/7cDujE',
                        'https://www.youtube.com/watch?v=m8e-FF8MsqU')

lord_of_the_rings = media.Movie('The Lord of the Rings',
                                'A hobbit goes on a quest to destroy the ring',
                                'http://goo.gl/DvZrog',
                                'https://www.youtube.com/watch?v=V75dMMIW2B4')

die_hard = media.Movie('Die Hard',
                       'John McClane tries to save his wife.',
                       'http://goo.gl/iOvSdo',
                       'https://www.youtube.com/watch?v=2TQ-pOvI6Xo')

dark_knight = media.Movie('The Dark Knight',
                          'Batman fights the Joker.',
                          'http://goo.gl/5ptAW2',
                          'https://www.youtube.com/watch?v=EXeTwQWrcwY')

hunger_games = media.Movie('Hunger Games',
                           'Katniss Everdeen plays in the Hunger Games',
                           'http://goo.gl/VDWgRa',
                           'https://www.youtube.com/watch?v=PbA63a7H0bo')

# Store Movie instances into list
movies = [toy_story, lord_of_the_rings, die_hard, dark_knight, hunger_games]

# Run open_movies_page from fresh_tomatoes to populate browser
fresh_tomatoes.open_movies_page(movies)
