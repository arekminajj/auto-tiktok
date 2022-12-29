import ffmpeg
import subprocess
import subtitles


def addVoiceoverAndSubtitlesToVideo():
    # generate subtitles
    subtitles.generateSubtitles()

    input_video = ffmpeg.input('././files/RAW_VIDEO.mp4')
    input_audio = ffmpeg.input('././files/voice.mp3')
    ffmpeg.concat(input_video.filter("subtitles", '././files/subtitles.srt', force_style="Alignment=10"),
                  input_audio, v=1, a=1).output('././files/video_final.mp4').run()

    print('video has been saved in: ././files/video_final.mp4')
