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
        return 'НОМЕР ВАГОНА НЕ ВЕРЕН'

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
        return 'Код ЕСР станции НЕ ВЕРЕН'

def checkFormatMessageSPhrase(messagePhraseCheck):
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
    fieldMax = {'200':12, '201':13, '202':11, '203':12,'205':11, '000':0}
        

    if len(messagePhraseCheck[0]) == numberCharactersField3:
        fieldTrue +=1
    else:
        messagePhraseCheck[0] = '000'
    

    if (len(messagePhraseCheck[1]) == numberCharactersField4 or len(messagePhraseCheck[numberField]) == numberCharactersField9):
        fieldTrue +=1
    else:
        messagePhraseCheck[1] = '0000'

    # if (numberField > 1 and numberField < 4) or numberField == 5:
    if len(messagePhraseCheck[2]) == numberCharactersField4:
        fieldTrue +=1
    else:
        messagePhraseCheck[2] = '0000'
    
    if len(messagePhraseCheck[3]) == numberCharactersField4:
        fieldTrue +=1
    else:
        messagePhraseCheck[3] = '0000'

    if (len(messagePhraseCheck[4]) == numberCharactersField2 or len(messagePhraseCheck[4]) == numberCharactersField3):
        fieldTrue +=1
    else:
        messagePhraseCheck[4] = '00'
    
    if len(messagePhraseCheck[5]) == numberCharactersField4:
        fieldTrue +=1
    else:
        messagePhraseCheck[5] = '0000'
    
    if (len(messagePhraseCheck[6]) == numberCharactersField4 or len(messagePhraseCheck[6]) == numberCharactersField8 
                                                                    or len(messagePhraseCheck[6]) == numberCharactersField9):
        fieldTrue +=1
    else:
        messagePhraseCheck[6] = '0000'

    for numberField in range(7, 11):
        if len(messagePhraseCheck[numberField]) == numberCharactersField2:
            fieldTrue +=1
        else:
            messagePhraseCheck[numberField] = '00'

    if fieldMax.get(messagePhraseCheck[0])-1 > 10:
        if len(messagePhraseCheck) == fieldMax.get(messagePhraseCheck[0]):
            if len(messagePhraseCheck[11]) == numberCharactersField5:
                fieldTrue +=1
            else:
                messagePhraseCheck[11] = '00000'
        else:
            messagePhraseCheck.append('00000')
    
    if fieldMax.get(messagePhraseCheck[0])-1 > 11:
        if len(messagePhraseCheck[12]) == numberCharactersField1:
            fieldTrue +=1
        else:
            messagePhraseCheck[12] = '0'
    if fieldMax.get(messagePhraseCheck[0])-1 > 12:
        if len(messagePhraseCheck[12]) == numberCharactersField1:
            fieldTrue +=1
        else:
            messagePhraseCheck[12] = '0'

    if fieldTrue == fieldMax.get(messagePhraseCheck[0]):
        resulFormat = 'МАКЕТ ВЕРЕН'
    else:
        resulFormat = 'ОШИБКА МАКЕТА СООБЩЕНИЯ'    

    return resulFormat, messagePhraseCheck

def checkFormatMessageIPhrase(messageIPhraseCheck):
    """
    Форматный контроль информационной фразы сообщений
    """
    IPhraseFieldTrue = 0
    IPhraseNumberField = 0
    IPhraseFieldMax = 8
    IPhraseColumnSet = {0:3, 1:5, 2:1, 3:2, 4:2, 5:4, 6:5, 7:2}
    if IPhraseFieldMax == len(messageIPhraseCheck):
        for IPhraseNumberField in range(0,IPhraseFieldMax):
            if IPhraseNumberField < IPhraseFieldMax-1 and IPhraseColumnSet.get(IPhraseNumberField) == len(messageIPhraseCheck[IPhraseNumberField]):
               IPhraseFieldTrue +=1
            if IPhraseNumberField == IPhraseFieldMax-1 and IPhraseColumnSet.get(IPhraseNumberField) < len(messageIPhraseCheck[IPhraseNumberField]):
               IPhraseFieldTrue +=1

        if IPhraseFieldTrue == IPhraseFieldMax:
            resulFormat = 'МАКЕТ ВЕРЕН'
        else:
            resulFormat = 'ОШИБКА МАКЕТА СООБЩЕНИЯ'    
    else:
            resulFormat = 'ОШИБКА МАКЕТА СООБЩЕНИЯ'
    return resulFormat

def addingMessage(messageSPhraseAdd):
    """Добавление недостающих элементов до полного набора полей общего формата сообщений.
    За полный набор полей общего формата сообщений принимаю набор полей сообщения 201
    """
    if messageSPhraseAdd[0] == '200':
        messageSPhraseAdd.append('0')
    elif messageSPhraseAdd[0] == '202' or messageSPhraseAdd[0] == '205':
        messageSPhraseAdd.append('00/00')
        messageSPhraseAdd.append('0')
    elif messageSPhraseAdd[0] == '203':
        messageSPhraseAdd.append('0')
    pass
    return messageSPhraseAdd        

def checkQuantityRoleStation(checkRoleStation: list, role: str):
    """
    Считет кол-во станций с заданой ролью
    """
    quantity = 0
    for i in checkRoleStation:
        if i[:1] == role:
            quantity += 1
    return quantity

def checkLogicalMessage(numberStation):
    # Логический контроль сообщения
                # if listMessages[-1][0] == '000':
                #     fileTXTResult.write('Сообщение не проверется, ОШИБКА МАКЕТА\n')
                #     return numberStation
                pass
                if (listMessages[-1][0] == '202' or (listMessages[-1][0] == '205' and numberStation == 0)  
                                                or (listMessages[-1][0] == '201' and numberStation != 0)): 
                    numberStation += 1
                
                if listMessages[-1][1] != '000':
                    if listMessages[-1][1] !=  stations[0][numberStation-1]: # проверка станции передачи сообщения
                        fileTXTResult.write(stations[0][numberStation-1] + ' -----Станция передачи сообщение НЕ СООТВЕТСТВУЕТ маршруту следования\n')
                    else: 
                        fileTXTResult.write(stations[0][numberStation-1] + ' Станция передачи сообщение соответствует маршруту следования\n')
                else:
                    fileTXTResult.write('ОШИБКА МАКЕТА. Код сообщения не проверяется')
                    
                # проверка номера поезда через кол-во технических станций и междор стыков в маршруте
                if numberStation == 1:
                    if (listMessages[-1][1][:1] == '2' and quantityTechnStation >= 3  # кол-во сорт и участ ст-ий >= 3
                                                    and quantityBoardStation == 0  # кол-во междор стыков нет
                                                or (quantityTechnStation >=2 # кол-во сорт и участ ст-ий >= 2
                                                    and quantityBoardStation > 0)): # кол-во междор стыков > 0
                        fileTXTResult.write('\t\t\t Кол- во техн станций на маршруте движения ' + str(quantityTechnStation) +
                                            ', кол-во междор стыков ' + str(quantityBoardStation) +' поезд сквозной \n')
                    else:
                        fileTXTResult.write('\t\t\t Кол- во техн станций на маршруте движения ' + str(quantityTechnStation) +
                                            ', кол-во междор стыков ' + str(quantityBoardStation) +' поезд не сквозной \n')
                else: 
                    if (listMessages[-2][2] == listMessages[-1][2]
                        or int(listMessages[-2][2]) == int(listMessages[-1][2])+1
                        or int(listMessages[-2][2]) == int(listMessages[-1][2])-1):
                        fileTXTResult.write('\t Номер поезда соответствует предыдущему сообщению\n\n')
                    else:
                        fileTXTResult.write('\t -----Номер поезда НЕ СООТВЕТСТВУЕТ предыдущему сообщению\n\n')
                pass
                return numberStation



""" def clearPartMessage(messageSPhrase, messageIPhrase, message):
    messageSPhrase.clear()
    messageIPhrase.clear()
    message.clear()
    return messageSPhrase, messageIPhrase, message """

# os.chdir('Для проверки//')
pathForCheck = 'Для проверки//' # папка хранения проверяемых файлов
pathPastCheck = 'После проверки//' # папка хранения результатов проверки
numberErrors = 0 
dictStation = {}
stations = []
messageSPhrase = []
messageIPhrase = []
messageSPhraseEmpty = ['000', '0000', '0000', '0000', '000', '0000', '0000', '00', '00', '00', '00', '00/00', '0']
messageIPhraseEmpty = ['000','00000','0','00','00','0000','00000','00']
message = []
messageTemp = []
listMessages = []
roleStations = []

# dictTest = {22000:[23000], 230000:[22000,24000]}
pass
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
                if res == 'НОМЕР ВАГОНА НЕ ВЕРЕН':
                    numberErrors += 1
                    fileTXTResult.write(lineTXT + ' '+ res+'. Ошибка '+ str(numberErrors)+'\n')
                else:
                    fileTXTResult.write(lineTXT + ' ' + res + '\n')
        fileTXTResult.write('#\n')
        # обработка списка кодов станций
        for i in fileTXT:
            lineTXT = i.strip()
            if lineTXT == '':
                continue
            if lineTXT == '#':
                break
            else:
                dictStation[lineTXT[3:7]] = lineTXT[:2]
                if len(dictStation) == 1:
                    setStation = {lineTXT[3:7]}
                else:
                    setStation.add(lineTXT[3:7])
                if len(dictStation) != len(setStation):
                    numberErrors += 1
                    fileTXTResult.write(lineTXT + '\t\t\tкод станции ' + lineTXT[3:7] +' повторяется. Ошибка '
                    + str(numberErrors) + '\n')
                    
                    del dictStation[lineTXT[:2]]
                
                resStation = checkStation(lineTXT[3:])
                if resStation == 'Код ЕСР станции НЕ ВЕРЕН':
                    numberErrors += 1
                    fileTXTResult.write(lineTXT + ' ' + resStation + '. Ошибка ' + str(numberErrors) + '\n')
                else:
                    fileTXTResult.write(lineTXT + ' ' + resStation + '\n')
        fileTXTResult.write('#\n')
        # обработка описания движения поездов
        pass
        for i in fileTXT:
            lineTXT = i.strip()
            if lineTXT == '':
                continue
            
            elif lineTXT[0] == '!':
                stations.clear()
                roleStations.clear()
                stations = [lineTXT[1:].split()]
                numberStation = 0
                for station in stations[0]:
                    roleStations.append(dictStation.get(station))
                stations.append(roleStations)
                fileTXTResult.write('\n'+lineTXT + '\t\t\tСПИСОК СТАНЦИЙ СФОРМИРОВАН\n\n')
                listMessages.clear()
                quantityTechnStation = checkQuantityRoleStation(roleStations, '1') + checkQuantityRoleStation(roleStations, '2')
                quantityBoardStation = checkQuantityRoleStation(roleStations, '5')

            elif (lineTXT[:2] == '(:'and lineTXT[-2:] != ':)'):
                messageSPhrase.clear()
                messageIPhrase.clear()
                message.clear() 
                messageTemp = lineTXT[2:].split()
                resultCheckFormat, messageSPhrase = checkFormatMessageSPhrase(messageTemp)
                fileTXTResult.write(lineTXT + '\t\t\t' + resultCheckFormat + '\n')
                message = addingMessage(messageSPhrase)
            
            elif lineTXT[:2] == '(:'and lineTXT[-2:] == ':)':
                messageTemp = lineTXT[2:-2].split()
                resultCheckFormat, messageSPhrase = checkFormatMessageSPhrase(messageTemp)    
                
                '''if resultCheckFormat == 'МАКЕТ ВЕРЕН':
                    messageSPhrase = messageTemp 
                else:
                    messageSPhrase = messageSPhraseEmpty.copy()'''
                fileTXTResult.write(lineTXT + '\t\t\t' + resultCheckFormat + '\n\n')
                message = addingMessage(messageSPhrase) + messageIPhraseEmpty.copy()
                listMessages.append(message.copy())
                
                numberStation = checkLogicalMessage(numberStation)
            
            elif lineTXT[:2] != '(:'and lineTXT[-2:] == ':)':
                messageTemp = lineTXT[:-2].split()
                resultCheckFormat = checkFormatMessageIPhrase(messageTemp)    
                if resultCheckFormat == 'МАКЕТ ВЕРЕН':
                    messageIPhrase = messageTemp
                else:
                    messageIPhrase = messageIPhraseEmpty.copy()
                fileTXTResult.write(lineTXT + '\t\t\t' + resultCheckFormat + '\n\n')
                message = message + messageIPhrase
                listMessages.append(message.copy())

                pass
                numberStation = checkLogicalMessage(numberStation)
                    
                
            else:
                fileTXTResult.write(lineTXT + '\t\t\tстрока не является частью сообщения\n\n')
            pass
            
        
        
        
        pass
        fileTXT.close()
        fileTXTResult.close()
print('\nОбработка завершена')
pass