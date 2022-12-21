import ffmpeg

def addVoiceoverToVideo():
    input_video = ffmpeg.input('./files/RAW_VIDEO.mp4')
    input_audio = ffmpeg.input('./files/voice.mp3')

    ffmpeg.concat(input_video, input_audio, v=1, a=1).output('./files/video_with_audio_over.mp4').run()

    print('video has been saved in: ' + './files/video_with_audio_over.mp4')

def addSubtitlesToVideo():
    print('TODO')
