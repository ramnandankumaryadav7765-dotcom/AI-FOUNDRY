"""A simple media queue with Movies, Series, and Podcasts."""


class Movie:
    def __init__(self, title, minutes):
        self.title = title
        self.minutes = minutes

    def calculate_watch_time(self):
        return self.minutes


class Series:
    def __init__(self, title, total_episodes, episodes_watched, avg_episode_minutes):
        self.title = title
        self.total_episodes = total_episodes
        self.episodes_watched = episodes_watched
        self.avg_episode_minutes = avg_episode_minutes

    def calculate_watch_time(self):
        return self.episodes_watched * self.avg_episode_minutes

    @property
    def progress_percentage(self):
        if self.total_episodes == 0:
            return 0
        return self.episodes_watched / self.total_episodes * 100


class Podcast:
    def __init__(self, host, total_episodes, episodes_listened, avg_episode_minutes):
        self.host = host
        self.total_episodes = total_episodes
        self.episodes_listened = episodes_listened
        self.avg_episode_minutes = avg_episode_minutes

    def calculate_watch_time(self):
        return self.episodes_listened * self.avg_episode_minutes

    @property
    def progress_percentage(self):
        if self.total_episodes == 0:
            return 0
        return self.episodes_listened / self.total_episodes * 100

    @property
    def completion_badge(self):
        if self.episodes_listened == self.total_episodes:
            return "🏆 Finished"
        return ""


class QueueManager:
    def __init__(self):
        self.media = []

    def add_media(self, item):
        self.media.append(item)


def _add_media_menu(queue):
    print("\nAdd media: 1. Movie  2. Series  3. Podcast")
    choice = input("Choose 1, 2, or 3: ").strip()

    if choice == "1":
        title = input("Movie title: ").strip()
        minutes = int(input("Movie length in minutes: "))
        queue.add_media(Movie(title, minutes))
    elif choice == "2":
        title = input("Series title: ").strip()
        total = int(input("Total episodes: "))
        watched = int(input("Episodes watched: "))
        average = int(input("Average episode length in minutes: "))
        queue.add_media(Series(title, total, watched, average))
    elif choice == "3":
        host = input("Podcast host: ").strip()
        total = int(input("Total episodes: "))
        listened = int(input("Episodes listened: "))
        average = int(input("Average episode length in minutes: "))
        queue.add_media(Podcast(host, total, listened, average))
    else:
        print("Please choose 1, 2, or 3.")


def _render_table(queue):
    print("\nType      | Name / Host     | Watch time | Progress | Status")
    print("----------|-----------------|------------|----------|--------------")

    for item in queue.media:
        if isinstance(item, Movie):
            kind = "Movie"
            name = item.title
            watch_time = item.calculate_watch_time()
            progress = "—"
            status = ""
        elif isinstance(item, Series):
            kind = "Series"
            name = item.title
            watch_time = item.calculate_watch_time()
            progress = f"{item.progress_percentage:.0f}%"
            status = ""
        else:  # Podcast
            kind = "Podcast"
            name = item.host
            watch_time = item.calculate_watch_time()
            progress = f"{item.progress_percentage:.0f}%"
            status = item.completion_badge

        print(f"{kind:<9} | {name:<15} | {watch_time:>8} min | {progress:<8} | {status}")


def main():
    queue = QueueManager()

    while True:
        print("\n1. Add media   2. Show queue   3. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            _add_media_menu(queue)
        elif choice == "2":
            _render_table(queue)
        elif choice == "3":
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
