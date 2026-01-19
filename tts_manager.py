'''from TTS.api import TTS

tts=TTS("tts_models/en/ljspeech/tacotron2-DDC")

def save_output(text,output="output.wav"):
    tts.tts_to_file(text,file_path=output)
    return output
'''

from gtts import gTTS

def save_audio(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    return filename

