import fresh_tomatoes
import media

#Create multiple instances of Movie with favorite movie information

toy_story = media.Movie('The Matrix',
                        'A computer hackers learns about the true nature of his reality.',
                        'http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg',
                        'https://www.youtube.com/watch?v=m8e-FF8MsqU')

lord_of_the_rings = media.Movie('The Lord of the Rings',
                                'A hobbit embarks on a quest to destroy the ring',
                                'http://ia.media-imdb.com/images/M/MV5BNTEyMjAwMDU1OV5BMl5BanBnXkFtZTcwNDQyNTkxMw@@._V1_SY317_CR1,0,214,317_AL_.jpg',
                                'https://www.youtube.com/watch?v=V75dMMIW2B4')

die_hard = media.Movie('Die Hard',
                       'John McClane, officer of the NYPD, tries to save wife Holly Gennaro and several others, taken hostage by German terrorist Hans Gruber during a Christmas party at the Nakatomi Plaza in Los Angeles.',
                       'http://ia.media-imdb.com/images/M/MV5BMTY4ODM0OTc2M15BMl5BanBnXkFtZTcwNzE0MTk3OA@@._V1_SX214_AL_.jpg',
                       'https://www.youtube.com/watch?v=2TQ-pOvI6Xo')

the_dark_knight = media.Movie('The Dark Knight',
                              'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.',
                              'http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY317_CR0,0,214,317_AL_.jpg',
                              'https://www.youtube.com/watch?v=EXeTwQWrcwY')

hunger_games = media.Movie('Hunger Games',
                           'Katniss Everdeen voluntarily takes her younger sisters place in the Hunger Games, a televised fight to the death in which two teenagers from each of the twelve Districts of Panem are chosen at random to compete.',
                           'http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg',
                           'https://www.youtube.com/watch?v=PbA63a7H0bo')

#Store Movie instances into list
movies = [toy_story, lord_of_the_rings, die_hard, the_dark_knight, hunger_games]

#Run open_movies_page from fresh_tomatoes to populate browser
fresh_tomatoes.open_movies_page(movies)
