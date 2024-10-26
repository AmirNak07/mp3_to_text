# Converter MP3 to text

## Описание

Данный код является Python приложением на PyQt6 способное транскрибацировать аудиофайлы(а точнее .mp3). Для распознования речи использовались библиотека Vosk их модель синтеза речи.

## Установка

1. Склонировать репозиторий

    ```bash
    git clone git@github.com:AmirNak07/mp3_to_text.git
    ```

    Далее переходим в директорию с проектом. Рекомендуется использовать виртуальное окружение Python(virtualvenv). Если вы используете глобальный интерпретатор, то этапы 2-3 можете пропустить

2. Создание виртуального окржения

    ```bash
    python3.12 -m venv .venv
    ```

    Возможно использовать другие версии(я использовал 3.12.3)

3. Активация виртуального окружения

    Для Windows:

    ```powershell
    .venv\Scripts\activate
    ```

    Для Linux/Mac OS:

    ```bash
    source .venv/bin/activate
    ```

4. Подтянуть все зависимости

    ```bash
    pip install -r requirements.txt
    ```

5. Скачать модель

    Переходим по данной [ссылке](https://alphacephei.com/vosk/models) и скачиваем архив с нужной моделью в папку с проектом, разархивируем и называем "model".

## Запуск(обычный)

```bash
python app.py
```

[©Amir Nakhushev](https://github.com/AmirNak07)
