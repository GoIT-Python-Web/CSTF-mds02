class VideoFile:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def decode(self):
        print(f"Decoding video file {self.name}...")


class AudioFile:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def decode(self):
        print(f"Decoding audio file {self.name}...")


class SubtitleFile:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def decode(self):
        print(f"Adding subtitle file {self.name}...")


class VideoPlayer:  # Facade
    def __init__(self, video_file: VideoFile, audio_file: AudioFile, subtitle_file: SubtitleFile):
        self.video_file = video_file
        self.audio_file = audio_file
        self.subtitle_file = subtitle_file

    def play(self):
        self.video_file.decode()
        self.audio_file.decode()
        self.subtitle_file.decode()


if __name__ == "__main__":
    video_file = VideoFile("video.mp4", 1000)
    audio_file = AudioFile("audio.mp3", 500)
    subtitle_file = SubtitleFile("subtitle.srt", 200)
    player = VideoPlayer(video_file, audio_file, subtitle_file)
    player.play()
