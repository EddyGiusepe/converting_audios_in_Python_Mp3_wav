'''
Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro

Link de estudo: https://www.youtube.com/watch?v=M4Vop5Qz0ZM
'''
from pydub import AudioSegment

wav1 = AudioSegment.from_wav("/home/eddygiusepe/2_praticando_Python/Conversao_de_Pastas_AUDIO_Python/ACV0004MODIFY.wav")
wav1.export("teste_audio.wav", format="wav")


#import os; print(os.environ["PATH"].split(os.pathsep))