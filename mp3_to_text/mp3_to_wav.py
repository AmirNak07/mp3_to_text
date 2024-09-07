from pydub import AudioSegment


class ConvertMp3ToWav():
    def __init__(self, src: str, dst: str) -> None:
        self.src = src
        self.dst = dst
        self.sound = AudioSegment.from_mp3(src)

    def export(self):
        self.sound.export(self.dst, format="wav")
