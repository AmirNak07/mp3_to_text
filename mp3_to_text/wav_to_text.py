import wave
import os

from vosk import Model, KaldiRecognizer


class ConvertWavToText():
    def __init__(self, inFileName, outFileResults) -> None:
        self.inFileName = inFileName
        self.outFileResults = outFileResults

    def wav_to_text(self) -> str:
        wf = wave.open(self.inFileName, "rb")
        results = ""

        try:
            model = Model("model")
        except Exception as e:
            print(e)
            print('Hint: Check yout "model" directory')
        recognizer = KaldiRecognizer(model, wf.getframerate())
        recognizer.SetWords(True)

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                recognizerResult = recognizer.Result()
                results += recognizerResult
            else:
                # print(recognizer.PartialResult())
                pass

        results += recognizer.FinalResult()
        results = results[results.index('"text"'):].replace('"text" : "', "").replace('"\n}', "")
        return results

    def export(self, data):
        with open(self.outFileResults, "w", encoding="utf-8") as file:
            file.write(data)

    def delete_wav(self):
        os.remove(self.inFileName)
