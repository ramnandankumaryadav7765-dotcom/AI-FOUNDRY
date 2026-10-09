"""A small example of enums, inheritance, properties, and polymorphism."""

from abc import ABC, abstractmethod
from enum import Enum


class Mood(Enum):
    HAPPY = 1
    SAD = 2
    BORED = 3
    EXCITED = 4


class WatchStatus(Enum):
    PLANNED = "Planned"
    WATCHING = "Watching"
    COMPLETED = "Completed"


class Playable(ABC):
    @abstractmethod
    def play(self):
        """Start playing this media item."""
        pass


class MediaItem(ABC):
    def __init__(self, title, status=WatchStatus.PLANNED):
        self.title = title
        self.status = status

    def mark_completed(self):
        self.status = WatchStatus.COMPLETED

    @abstractmethod
    def calculate_watch_time(self):
        """Return the watched time in minutes."""
        pass

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "title": self.title,
            "status": self.status.value,
        }


class Movie(MediaItem, Playable):
    def __init__(self, title, runtime, status=WatchStatus.PLANNED):
        super().__init__(title, status)
        self.runtime = runtime

    def calculate_watch_time(self):
        return self.runtime

    def play(self):
        return f"Playing movie: {self.title}"

    def to_dict(self):
        movie_data = super().to_dict()
        movie_data["runtime"] = self.runtime
        return movie_data

    def __str__(self):
        return f"Movie(title={self.title!r}, runtime={self.runtime} min, status={self.status.value})"


class Series(MediaItem, Playable):
    def __init__(self, title, total_episodes, episodes_watched, avg_episode_runtime,
                 status=WatchStatus.PLANNED):
        super().__init__(title, status)
        self.total_episodes = total_episodes
        self.episodes_watched = episodes_watched
        self.avg_episode_runtime = avg_episode_runtime

    @property
    def total_duration(self):
        return self.total_episodes * self.avg_episode_runtime

    @property
    def remaining_time(self):
        episodes_left = self.total_episodes - self.episodes_watched
        return episodes_left * self.avg_episode_runtime

    def calculate_watch_time(self):
        return self.episodes_watched * self.avg_episode_runtime

    def play(self):
        return f"Playing series: {self.title}"

    def to_dict(self):
        series_data = super().to_dict()
        series_data.update({
            "total_episodes": self.total_episodes,
            "episodes_watched": self.episodes_watched,
            "avg_episode_runtime": self.avg_episode_runtime,
        })
        return series_data

    def __str__(self):
        return (
            f"Series(title={self.title!r}, episodes={self.episodes_watched}/"
            f"{self.total_episodes}, status={self.status.value})"
        )


class Anime(Series):
    def __init__(self, title, total_episodes, episodes_watched,
                 avg_episode_runtime, has_dub=False, status=WatchStatus.PLANNED):
        super().__init__(title, total_episodes, episodes_watched,
                         avg_episode_runtime, status)
        self.has_dub = has_dub

    def to_dict(self):
        anime_data = super().to_dict()
        anime_data["has_dub"] = self.has_dub
        return anime_data


if __name__ == "__main__":
    # 1. Print each enum member's name and value.
    print("Moods:")
    for mood in Mood:
        print(mood.name, mood.value)

    # 2. Create favorite titles using keyword arguments and print them.
    movie = Movie(title="Finding Nemo", runtime=100)
    series = Series(
        title="Stranger Things",
        total_episodes=34,
        episodes_watched=10,
        avg_episode_runtime=50,
    )
    print("\nMy media:")
    print(movie)
    print(series)

    # 3-4. Show the Series properties.
    print("\nSeries total duration:", series.total_duration, "minutes")
    print("Series remaining time:", series.remaining_time, "minutes")

    # 5. Mark the movie completed. Its watch time is still its runtime.
    movie.mark_completed()
    print("\nMovie status:", movie.status.value)
    print("Movie watch time:", movie.calculate_watch_time(), "minutes")

    # 6. Movie, Series, and Anime respond to the same method call.
    anime = Anime(
        title="Fullmetal Alchemist: Brotherhood",
        total_episodes=64,
        episodes_watched=64,
        avg_episode_runtime=24,
        has_dub=True,
    )
    media_list = [movie, series, anime]
    print("\nWatch times (polymorphism):")
    for item in media_list:
        print(item.title, "=", item.calculate_watch_time(), "minutes")

    # 7. Each playable media class provides its own play() message.
    print("\nPlay messages:")
    for item in media_list:
        print(item.play())

    # 8. Example dictionary output for one Movie.
    print("\nMovie dictionary:")
    print(movie.to_dict())
