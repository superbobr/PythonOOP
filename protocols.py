from typing import Protocol


class Playable(Protocol):
    def play(self) -> None:
        pass


class MusicTrack:
    def __init__(self, title):
        self.title = title

    def play(self):
        print(f'Играет трек: {self.title}')


class Video:
    def __init__(self, title):
        self.title = title

    def play(self):
        print(f'Воспроизводится видео: {self.title}')


def play_all(items: list[Playable]) -> None:
    for item in items:
        item.play()


user_audio = MusicTrack(input())
user_video = Video(input())

play_all([user_audio, user_video])