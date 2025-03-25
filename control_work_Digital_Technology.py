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
        return 'Номер вагона верен'
    else: 
        return 'Номер вагона не верен'

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
        return 'Код ЕСР станции верен'
    else: 
        return 'Код ЕСР станции не верен'

def checkFormatMessageSPhrase(messagePhrase):
    """
    Форматный контроль служебной фразы сообщений
    """
    numberCharactersField1 = 1
    numberCharactersField2 = 2
    numberCharactersField3 = 3
    numberCharactersField4 = 4
    numberCharactersField5 = 5
    numberCharactersField8 = 8
    numberCharactersField9 = 9
    fieldTrue = 0
    numberField = 0
    fieldMax = {'200':12, '201':13, '202':11, '203':12,'205':11 }
    if fieldMax.get(messageSPhrase[0]) == len(messageSPhrase):
        for numberField in range(0,fieldMax.get(messageSPhrase[0])):
            if numberField == 0 and len(messageSPhrase[numberField]) == numberCharactersField3:
                fieldTrue +=1
            elif numberField == 1 and (len(messageSPhrase[numberField]) == numberCharactersField4 or len(messageSPhrase[numberField]) == numberCharactersField9):
                fieldTrue +=1
            elif ((numberField > 1 and numberField < 4) or numberField == numberCharactersField5) and len(messageSPhrase[numberField]) == numberCharactersField4:
                fieldTrue +=1
            elif numberField == 4 and (len(messageSPhrase[numberField]) == numberCharactersField2 or len(messageSPhrase[numberField]) == numberCharactersField3):
                fieldTrue +=1
            elif numberField == 6 and (len(messageSPhrase[numberField]) == numberCharactersField4 or len(messageSPhrase[numberField]) == numberCharactersField8 
                                                                            or len(messageSPhrase[numberField]) == numberCharactersField9):
                fieldTrue +=1
            elif numberField > 6 and numberField < 11 and len(messageSPhrase[numberField]) == numberCharactersField2:
                fieldTrue +=1
            elif numberField == 11 and len(messageSPhrase[numberField]) == numberCharactersField5:
                fieldTrue +=1
            elif numberField == 12 and len(messageSPhrase[numberField]) == numberCharactersField1:
                fieldTrue +=1
        if fieldTrue == fieldMax.get(messageSPhrase[0]):
            resulFormat = 'МАКЕТ ВЕРЕН'
        else:
            resulFormat = 'ОШИБКА МАКЕТА СООБЩЕНИЯ'    
    else:
            resulFormat = 'ОШИБКА МАКЕТА СООБЩЕНИЯ'
    return resulFormat

def checkFormatMessageIPhrase(messageIhrase):
    """
    Форматный контроль информационной фразы сообщений
    """
    IPhraseFieldTrue = 0
    IPhraseNumberField = 0
    IPhraseFieldMax = 8
    IPhraseColumnSet = {0:3, 1:5, 2:1, 3:2, 4:2, 5:4, 6:5, 7:2}
    if IPhraseFieldMax == len(messageIPhrase):
        for IPhraseNumberField in range(0,IPhraseFieldMax):
            if IPhraseNumberField < IPhraseFieldMax-1 and IPhraseColumnSet.get(IPhraseNumberField) == len(messageIPhrase[IPhraseNumberField]):
               IPhraseFieldTrue +=1
            if IPhraseNumberField == IPhraseFieldMax-1 and IPhraseColumnSet.get(IPhraseNumberField) < len(messageIPhrase[IPhraseNumberField]):
               IPhraseFieldTrue +=1

        if IPhraseFieldTrue == IPhraseFieldMax:
            resulFormat = 'МАКЕТ ВЕРЕН'
        else:
            resulFormat = 'ОШИБКА МАКЕТА СООБЩЕНИЯ'    
    else:
            resulFormat = 'ОШИБКА МАКЕТА СООБЩЕНИЯ'
    return resulFormat

def creatingListMessages():
    """Добавление недостающих элементов до полного набора полей общего формата сообщений
    за полный набор полей общего формата сообщений принимаю набор полей сообщения 201
    """
    if messageSPhrase[0] == '200' or messageSPhrase[0] == '205':
        messageSPhrase.append('0')
    elif messageSPhrase[0] == '202':
        messageSPhrase.append('00/00')
        messageSPhrase.append('0')
    elif messageSPhrase[0] == '203':
        messageSPhrase.append('0')
    pass
            

# os.chdir('Для проверки//')
pathForCheck = 'Для проверки//' # папка хранения проверяемых файлов
pathPastCheck = 'После проверки//' # папка хранения результатов проверки
dictStation = {}
stations = []
messageSPhrase = []
messageIPhrase = []
messageList = []
messageList = []

fileList = os.listdir(pathForCheck) 
for nameFileTXT in fileList:
    if nameFileTXT[-3:] != 'txt': # открываем файлы только с расширением TXT
        continue
    else:
        fileTXT = open(pathForCheck+nameFileTXT, 'r', encoding='cp1251') # открытие проверяемого файла 
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
                    fileTXTResult.write(lineTXT + '\t\t\tкод станции ' + lineTXT[3:7] +' повторяется\n')
                    del dictStation[lineTXT[:2]]
                
                res = checkStation(lineTXT[3:])
                fileTXTResult.write(lineTXT + ' ' + res + '\n')
        fileTXTResult.write('#\n')
        # обработка описания движения поездов
        for i in fileTXT:
            lineTXT = i.strip()
            if lineTXT == '':
                continue
            
            elif lineTXT[0] == '!':
                stations.clear()
                stations = lineTXT[1:].split()
                fileTXTResult.write(lineTXT + '\t\t\tСПИСОК СТАНЦИЙ СФОРМИРОВАН\n\n')

            elif (lineTXT[:2] == '(:'and lineTXT[-2:] != ':)'):
                messageSPhrase.clear()
                messageSPhrase = lineTXT[2:].split()
                resultCheckFormat = checkFormatMessageSPhrase(messageSPhrase)    
                fileTXTResult.write(lineTXT + '\t\t\t' + resultCheckFormat + '\n')
            
            elif lineTXT[:2] == '(:'and lineTXT[-2:] == ':)':
                messageSPhrase.clear()
                messageSPhrase = lineTXT[2:-2].split()
                resultCheckFormat = checkFormatMessageSPhrase(messageSPhrase)    
                fileTXTResult.write(lineTXT + '\t\t\t' + resultCheckFormat + '\n')
            
            elif lineTXT[:2] != '(:'and lineTXT[-2:] == ':)':
                messageIPhrase.clear()
                messageIPhrase = lineTXT[:-2].split()
                resultCheckFormat = checkFormatMessageIPhrase(messageIPhrase)    
                fileTXTResult.write(lineTXT + '\t\t\t' + resultCheckFormat + '\n\n')
            
                pass
            
                
            
            # добавление недостающих элементов до полного набора полей общего формата сообщений
            # за полный набор полей общего формата сообщений принимаю набор полей сообщения 201
                '''
                if messageSPhrase[0] == '200' or messageSPhrase[0] == '205':
                    messageSPhrase.append('0')
                elif messageSPhrase[0] == '202':
                    messageSPhrase.append('00/00')
                    messageSPhrase.append('0')
                elif messageSPhrase[0] == '203':
                    messageSPhrase.append('0')
                    pass
                '''
                '''
                elif lineTXT[:2] != '(:'and lineTXT[-2:] == ':)':
                    messageIPhrase.clear()
                    messageIPhrase = lineTXT[:-2].split()
                    fileTXTResult.write(lineTXT + '\t\t\t\t\tстрока не обработана\n\n') '
                '''
            else:
                fileTXTResult.write(lineTXT + '\t\t\tстрока не является частью сообщения\n\n')

        pass
        fileTXT.close()
        fileTXTResult.close()
print('\nОбработка завершена')
pass