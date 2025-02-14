"""
Проверка контрольной работы по дисциплине "Цифровые технологии в профессональной деятельности"
"""
import os

#car = '50701077'
def checkNumber(car):
    """
    Проверка номера вагона
    """
    resultCar = 0
    for pos in range(8):
        if pos%2 == 0:
            if int(car[pos])*2 > 9:
                resultCar = resultCar + 1 + (int(car[pos])*2)%10
            else:
                resultCar = resultCar + int(car[pos])*2
        else: 
            resultCar = resultCar + int(car[pos])
    #print(resultCar)
    if resultCar % 10 == 0:
        return '+'
    else: 
        return '-'

#station = '781316'
def checkStation(station):
    """
    Проверка кода ЕСР станции
    """
    resultStation = 0
    for pos in range(5):
        resultStation = resultStation + (int(station[pos])*(pos+1))
    if resultStation % 11 > 9:
        resultStation = 0
        for pos in range(5):
            resultStation = resultStation + (int(station[pos])*(pos+3))
        if resultStation % 11 == 10:
            resultStation = 11
    #print(resultStation % 11, station[5])
    if (resultStation % 11) == int(station[5]):
        return '+'
    else: 
        return '-'

# os.chdir('Для проверки//')
pathForCheck = 'Для проверки//' # папка хранения проверяемых файлов
pathPastCheck = 'После проверки//' # папка хранения результатов проверки
dictStation = {}
stations = []
messageSPhrase = []
messageIPhrase = []

fileList = os.listdir(pathForCheck) 
for nameFileTXT in fileList:
    if nameFileTXT[-3:] != 'txt':
        continue
    else:
        fileTXT = open(pathForCheck+nameFileTXT, 'r', encoding='UTF-8') # открытие проверяемого файла 
        fileTXTResult = open(pathPastCheck+nameFileTXT[0:len(nameFileTXT)-4]+'_result'+'.txt', 'w', encoding='cp1251') # результат проверки
        # обработка номеров вагонов
        for i in fileTXT:
            lineTXT = i.strip()
            if lineTXT == '':
                continue
            if lineTXT == '#':
                break
            else:
                res = checkNumber(lineTXT)
                fileTXTResult.write(lineTXT + ' '+ res+'\n')
        fileTXTResult.write('#\n')
        # обработка списка кодов станций
        for i in fileTXT:
            lineTXT = i.strip()
            if lineTXT == '':
                continue
            if lineTXT == '#':
                break
            else:
                dictStation[lineTXT[:2]] = lineTXT[3:]
                if len(dictStation) == 1:
                    setStation = {lineTXT[3:7]}
                else:
                    setStation.add(lineTXT[3:7])
                if len(dictStation) != len(setStation):
                    fileTXTResult.write(lineTXT + ' код станции ' + lineTXT[3:7] +' повторяется\n')
                    del dictStation[lineTXT[:2]]
                    continue
                res = checkStation(lineTXT[3:])
                fileTXTResult.write(lineTXT + ' ' + res + '\n')
        fileTXTResult.write('#\n')
        # обработка описания движения поездов
        for i in fileTXT:
            lineTXT = i.strip()
            if lineTXT[0] == '!':
                stations.clear()
                stations = lineTXT[1:].split()
                continue
            elif lineTXT[:2] == '(:'and lineTXT[-2:] != ':)':
                messageSPhrase.clear()
                messageSPhrase = lineTXT[2:-1].split()
                continue
            elif lineTXT[:2] != '(:'and lineTXT[-2:] == ':)':
                messageIPhrase.clear()
                messageIPhrase = lineTXT[:-1].split()
                continue
            elif lineTXT[:2] == '(:'and lineTXT[-2:] == ':)':
                messageSPhrase.clear()
                messageSPhrase = lineTXT[:-1].split()
                continue
                pass
        fileTXT.close()
        fileTXTResult.close()
print('\nОбработка завершена')
pass