# coding=gbk
# link de estudo --> https://powersought.com/article/723477013/

import os
import wave
import numpy as np
import pylab as plt

CuttimeDef = 10  # truncado com 1s
# CutFrameNum =0


#path = r"..\test"
path = r"/home/eddygiusepe/5_praticando_Python/Conversao_de_Pastas_AUDIO_Python/testinho"
files = os.listdir(path)
print(files)
files = [path + "/" + f for f in files if f.endswith('.WAV')]
print(files)


def SetFileName(WavFileName):
    for i in range(len(files)):
        FileName = files[i]
        print("SetFileName File Name is ", FileName)
        FileName = WavFileName;


def CutFile():
    for i in range(len(files)):
        FileName = files[i]
        print("CutFile File Name is ", FileName)
        f = wave.open(r"" + FileName, "rb")
        params = f.getparams()
        print(params)
        nchannels, sampwidth, framerate, nframes = params[:4]
        CutFrameNum = framerate * CutTimeDef
        # Informa??es de formato ler
        # Tempo retorna as informa??es de formato de todos os arquivos WAV, retorna um componente: o número de canais, o número de posi??es de quantiza??o (unidade de byte),
        # #   Taxa, ponto de amostragem, tipo de compacta??o, descri??o do tipo de compacta??o. Os módulos de onda só suportam dados n?o compactados, para que você possa ignorar as duas últimas informa??es

        print("CutFrameNum=%d" % (CutFrameNum))
        print("nchannels=%d" % (nchannels))
        print("sampwidth=%d" % (sampwidth))
        print("framerate=%d" % (framerate))
        print("nframes=%d" % (nframes))
        str_data = f.readframes(nframes)
        F.Close()  # Converta os dados da forma de onda em uma matriz
    # Cutnum =nframes/framerate/CutTimeDef
    # Requer para converter os dados binários de leitura em uma matriz calculada de acordo com o número de canais e unidades de quantiza??o.
    wave_data = np.fromstring(str_data, dtype=np.short)
    wave_data.shape = -1, 2
    wave_data = wave_data.T
    temp_data = wave_data.T
    # StepNum = int(nframes/200)
    StepNum = CutFrameNum
    StepTotalNum = 0;
    haha = 0
    while StepTotalNum < nframes:
        # for j in range(int(Cutnum)):
        print("Stemp=%d" % (haha))
        FileName = "../testcutresults/" + files[i][-17:-4] + "-" + str(haha + 1) + ".WAV"
        print(FileName)
        temp_dataTemp = temp_data[StepNum * (haha):StepNum * (haha + 1)]
        haha = haha + 1;
        StepTotalNum = haha * StepNum;
        temp_dataTemp.shape = 1, -1
        Temp_datatemp = temp_datatemp.astype(np.short)  # abre documenta??o wav
    f = wave.open(FileName, "wb")  #
    # Configure o número de canais, bit de quantiza??o e frequência de amostragem
    f.setnchannels(nchannels)
    f.setsampwidth(sampwidth)
    f.setframerate(framerate)
    # Converter Wav_Data para Arquivo de Escrita de Dados Binários
    f.writeframes(temp_dataTemp.tostring())
    f.close()


if __name__ == '__main__':
    CutFile()

    print("Run Over")