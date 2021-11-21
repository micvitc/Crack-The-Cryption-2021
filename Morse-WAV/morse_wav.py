import string
import math
import wave
import struct

def main(msg):
  built_audio = AudioBuild(translateMessageToMorse(msg))
  first_word = makeListRemovePunctuationLower(msg)[0]
  save_wav("{}.wav".format(first_word), built_audio)

def makeListRemovePunctuationLower(msg):
  list_of_words = msg.split(' ')
  new_list = []
  exclude = set(string.punctuation)
  for w in list_of_words:
      new_list.append(''.join(ch.lower() for ch in w if ch not in exclude))
  return new_list

def AudioBuild(morseMessage):
  audio = []
  charList = list(morseMessage)
  for char in charList:
      if char == "-":
          audio = append_sinewave(audio, duration_milliseconds=300)
          audio = append_silence(audio)
      elif char == ".":
          audio = append_sinewave(audio, duration_milliseconds=100)
          audio = append_silence(audio)
      else:
          audio = append_silence(audio, duration_milliseconds=400)
  return audio

def translateMessageToMorse(msg):
  morseTransList = {
    'a':'.-',
    'b':'-...',
    'c':'-.-.',
    'd':'-..',
    'e':'.',
    'f':'..-.',
    'g':'--.',
    'h':'....',
    'i':'..',
    'j':'.---',
    'k':'-.-',
    'l':'.-..',
    'm':'--',
    'n':'-.',
    'o':'---',
    'p':'.--.',
    'q':'--.-',
    'r':'.-.',
    's':'...',
    't':'-',
    'u':'..-',
    'v':'...-',
    'w':'.--',
    'x':'-..-',
    'y':'-.--',
    'z':'--..',
    '0':'-----',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.'
  }
  ableList = makeListRemovePunctuationLower(msg)
  msg = []
  for word in ableList:
    trans_word = []
    for letter in word:
        trans_word.append(morseTransList[letter])
    msg.append(' '.join(trans_word))
  return " ".join(msg)


def append_silence(audio,
                   duration_milliseconds=200):
  
    sample_rate = 8000.0
    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)):
        audio.append(0.0)

    return audio


def append_sinewave(audio,
                    freq=650.0,
                    duration_milliseconds=500,
                    volume=1.0):

    sample_rate = 8000.0
    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)):
        audio.append(volume * math.sin(2 * math.pi * freq * ( x / sample_rate )))

    return audio


def save_wav(file_name, audio):
    # Open up a wav file
    wav_file=wave.open(file_name,"w")

    # wav params
    nchannels = 1
    sample_rate = 8000.0
    sampwidth = 2

   
    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

    for sample in audio:
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

    wav_file.close()

    return

if __name__ == '__main__':
    msg = input("Please input your message:\n")
    main(msg)
