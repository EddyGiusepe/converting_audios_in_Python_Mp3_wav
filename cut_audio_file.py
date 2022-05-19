from pydub import AudioSegment
from pydub.utils import make_chunks

## bluesfile 59.28s
audio = AudioSegment.from_file("28-2828-0002.WAV", "WAV")

size = 20000 ## Los milisegundos de corte

chunks = make_chunks(audio, size) ## Corta o áudio em trechos de 20 segundos

for i, chunk in enumerate(chunks):
## Enumeración, i es el índice, chunk es el archivo cortado
    chunk_name = "eddy{0}.WAV".format(i)
    print(chunk_name)
## Salvar documento
    chunk.export(chunk_name, format="WAV")