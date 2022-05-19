'''
Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro

Link de estudo: https://www.youtube.com/watch?v=M4Vop5Qz0ZM
'''
from pydub import AudioSegment
import glob
import os


for filename in glob.glob("*.WAV"):
    print(f"Convertendo {filename}")

    name, extension = os.path.splitext(filename)
    AudioSegment.from_wav(filename).export(name + ".wav", format="wav")

    print(f"{filename} convertido.")
