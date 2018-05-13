from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

# movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
# movies_csv = 'movies.csv'
# urlretrieve(movie_data, movies_csv)

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')

MOVIE_DATA

def get_movie_by_director():
    movie_dict = defaultdict(list)

    with open(MOVIE_DATA, encoding='utf-8') as movie_data:
        reader = csv.DictReader(movie_data)
        for row in reader:
            title = row['movie_title']
            year = row['title_year']
            score = row['imdb_score']
            movie_details = Movie(title = title, year = year, score = score)
            movie_dict[row['director_name']].append(movie_details)
    return movie_dict


def get_average_scores(directors):
    cnt = Counter()
    for director, movies in directors.items():
        cnt[director] += len(movies)

    return cnt.most_common(5)




def main():
    directors = get_movie_by_director()
    print(get_average_scores(directors))


main()


