import sys

from PyQt6.QtCore import Qt, QCoreApplication
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog

from mp3_to_text import ConvertMp3ToWav, ConvertWavToText


class Converter():
    def __init__(self, inputFile: str) -> None:
        self.inputFile = inputFile[0]
        self.filename = self.inputFile.split(".")[0]

    def mp3_to_wav(self):
        convert_mp3_to_wav = ConvertMp3ToWav(self.inputFile, f"{self.filename}.wav")
        convert_mp3_to_wav.export()

    def wav_to_text(self):
        convert_wav_to_text = ConvertWavToText(f"{self.filename}.wav", f"{self.filename}.txt")
        convert_wav_to_text.export(convert_wav_to_text.wav_to_text())
        convert_wav_to_text.delete_wav()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window Settings
        self.setWindowTitle("Конвертировать MP3 to текст")
        self.setFixedSize(450, 550)

        # Title
        self.title = QLabel("Конвертировать MP3 to текст")
        font = self.title.font()
        font.setPointSize(30)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Change File
        self.file_button = QPushButton("Выбрать файл")
        self.file_button.setFixedSize(150, 100)
        self.file_button.clicked.connect(self.choose_file_clicked)

        # Button
        self.button = QPushButton("Запустить")
        self.button.setFixedSize(150, 100)
        self.button.clicked.connect(self.loading)
        self.button.setDisabled(True)

        # Main Layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.file_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Widget
        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)

        self.setCentralWidget(self.widget)

    def choose_file_clicked(self):
        self.file = QFileDialog().getOpenFileName(None, "Выбрать аудио", ".", "Audio Files (*.mp3);;All Files (*)")
        filename = self.file[0].split("/")[-1]
        if filename != "":
            self.file_button.setText(f"Файл:\n{filename}")
            self.button.setDisabled(False)
        else:
            self.file_button.setText("Выбрать файл")
            self.button.setDisabled(True)

    def loading(self):
        try:
            converter = Converter(self.file)
            converter.mp3_to_wav()
            converter.wav_to_text()
        except Exception as e:
            print(e)
        finally:
            QCoreApplication.exit(0)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
