import ffmpeg
import subprocess
import subtitles

# TODO: ADD VOICEOVER AND SUBTITLES ON THE SAME GO.


def addVoiceoverToVideoSubprocess():
    subprocess.call(
        'ffmpeg -i ././files/RAW_VIDEO.mp4 -i ././files/voice.mp3  -filter_complex "[0:a]volume=0.2[A];[1:a][A]amerge[Aout]" -map 0:v -map [Aout] -y -shortest ././files/video_with_audio_over.mp4')
    print('video has been saved in: ' + '././files/video_with_audio_over.mp4')


def addVoiceoverToVideo():
    input_video = ffmpeg.input('././files/RAW_VIDEO.mp4')
    input_audio = ffmpeg.input('././files/voice.mp3')

    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(
        '././files/video_with_audio_over.mp4').run()

    print('video has been saved in: ' + '././files/video_with_audio_over.mp4')


def addSubtitlesToVideo():
    # generate subtitles
    subtitles.generateSubtitles()

    video = ffmpeg.input('././files/video_with_audio_over.mp4')
    audio = video.audio
    ffmpeg.concat(video.filter("subtitles", '././files/subtitles.srt'),
                  audio, v=1, a=1).output('././files/video_final.mp4').run()

    print('Video with subtitles generated in: ././files/video_final.mp4')
