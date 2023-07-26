from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        filtered = filter(lambda x: "," in x.get("country"), list_of_movies)
        filtered = filter(lambda x: x.get("rating_kinopoisk") not in ["", "0"], filtered)
        rate = list(map(lambda x: float(x.get("rating_kinopoisk")), filtered))
        return sum(rate) / len(rate)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        filtered = filter(lambda x: x.get("rating_kinopoisk") not in "", list_of_movies)
        filtered = filter(lambda x: float(x.get("rating_kinopoisk")) >= rating, filtered)
        counter = map(lambda x: x.get("name").count("и"), filtered)
        return sum(counter)
