import os


def deleteFiles():
    files_to_remove = [
        '././files/subtitles.srt',
        '././files/voice.mp3',
        '././files/video_final.mp4'
    ]

    for file in files_to_remove:
        try:
            os.remove(file)
            print('File: ' + file + ' has been removed')
        except FileNotFoundError:
            pass
