"""
Проверка контрольной работы по дисциплине "Цифровые технологии в профессональной деятельности"
"""
import os
import chardet
flagLoging = 0 # Флаг для логирования положительного результата проверки = 1
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
    global skipCheck

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
        
    if len(messagePhraseCheck) != fieldMax.get(messagePhraseCheck[0]):
        fieldTrue = 0
    else:    
        if len(messagePhraseCheck[0]) == numberCharactersField3:
            fieldTrue +=1
        else:
            pass # messagePhraseCheck[0] = '000'
        

        if (len(messagePhraseCheck[1]) == numberCharactersField4 or len(messagePhraseCheck[1]) == numberCharactersField9):
            fieldTrue +=1
        else:
            pass # messagePhraseCheck[1] = '0000'

        # if (numberField > 1 and numberField < 4) or numberField == 5:
        if len(messagePhraseCheck[2]) == numberCharactersField4:
            fieldTrue +=1
        else:
            pass # messagePhraseCheck[2] = '0000'
        
        if len(messagePhraseCheck[3]) == numberCharactersField4:
            fieldTrue +=1
        else:
            pass # messagePhraseCheck[3] = '0000'

        if (len(messagePhraseCheck[4]) == numberCharactersField2 or len(messagePhraseCheck[4]) == numberCharactersField3):
            fieldTrue +=1
        else:
            pass # messagePhraseCheck[4] = '00'
        
        if len(messagePhraseCheck[5]) == numberCharactersField4:
            fieldTrue +=1
        else:
            pass # messagePhraseCheck[5] = '0000'
        
        if (len(messagePhraseCheck[6]) == numberCharactersField4 or len(messagePhraseCheck[6]) == numberCharactersField8 
                                                                        or len(messagePhraseCheck[6]) == numberCharactersField9):
            fieldTrue +=1
        else:
            pass # messagePhraseCheck[6] = '0000'
        
        for numberField in range(7, 11):
            if len(messagePhraseCheck[numberField]) == numberCharactersField2:
                fieldTrue +=1
            else:
                pass # messagePhraseCheck[numberField] = '00'

        if fieldMax.get(messagePhraseCheck[0])-1 > 10:
            if len(messagePhraseCheck) == fieldMax.get(messagePhraseCheck[0]):
                if len(messagePhraseCheck[11]) == numberCharactersField5:
                    fieldTrue +=1
                else:
                    pass # messagePhraseCheck[11] = '00000'
            else:
                messagePhraseCheck.append('00000')
        
        if fieldMax.get(messagePhraseCheck[0])-1 > 11:
            if len(messagePhraseCheck[12]) == numberCharactersField1:
                fieldTrue +=1
            else:
                pass # messagePhraseCheck[12] = '0'
        if fieldMax.get(messagePhraseCheck[0])-1 > 12:
            if len(messagePhraseCheck[12]) == numberCharactersField1:
                fieldTrue +=1
            else:
                messagePhraseCheck[12] = '0'


    
    if fieldTrue == fieldMax.get(messagePhraseCheck[0]):
        resulFormat = 'МАКЕТ ВЕРЕН'
    else:
        resulFormat = 'ОШИБКА МАКЕТА СООБЩЕНИЯ'
        skipCheck += 1

    return resulFormat, messagePhraseCheck

def checkFormatMessageIPhrase(messageIPhraseCheck):
    """
    Форматный контроль информационной фразы сообщений
    """
    IPhraseFieldTrue = 0
    IPhraseNumberField = 0
    IPhraseFieldMax = 8
    IPhraseColumnSet = {0:3, 1:5, 2:1, 3:2, 4:2, 5:4, 6:5, 7:2} 
    if len(messageIPhraseCheck) == 8:
        for IPhraseNumberField in range(0,IPhraseFieldMax):
            if IPhraseNumberField < IPhraseFieldMax-1 and IPhraseColumnSet.get(IPhraseNumberField) == len(messageIPhraseCheck[IPhraseNumberField]):
                IPhraseFieldTrue +=1
            elif IPhraseNumberField < IPhraseFieldMax-1 and IPhraseColumnSet.get(IPhraseNumberField) != len(messageIPhraseCheck[IPhraseNumberField]):
                pass # messageIPhraseCheck[IPhraseNumberField] = '0' * IPhraseColumnSet.get(IPhraseNumberField)
            if IPhraseNumberField == IPhraseFieldMax-1 and IPhraseColumnSet.get(IPhraseNumberField) < len(messageIPhraseCheck[IPhraseNumberField]):
                IPhraseFieldTrue +=1
            elif IPhraseNumberField == IPhraseFieldMax-1 and IPhraseColumnSet.get(IPhraseNumberField) > len(messageIPhraseCheck[IPhraseNumberField]):
                pass # messageIPhraseCheck[IPhraseNumberField] = '0' * IPhraseColumnSet.get(IPhraseNumberField)
    else:
        IPhraseFieldTrue = len(messageIPhraseCheck)
    if IPhraseFieldTrue == IPhraseFieldMax:
        resulFormatIPhraseCheck = 'МАКЕТ ВЕРЕН'
    else:
        resulFormatIPhraseCheck = 'ОШИБКА МАКЕТА СООБЩЕНИЯ' 
        messageIPhraseCheck = messageIPhraseEmpty
    
    return resulFormatIPhraseCheck, messageIPhraseCheck

def addingMessage(messageSPhraseAdd):
    """Добавление недостающих элементов до полного набора полей общего формата сообщений.
    За полный набор полей общего формата сообщений принят набор полей сообщения 201
    """
    messageSPhraseEmpty = ['000', '0000', '0000', '0000', '000', '0000', '0000', '00', '00', '00', '00', '00/00', '9']
      
    for j in range(len(messageSPhraseAdd),13):
        messageSPhraseAdd.append(messageSPhraseEmpty[j])
    pass
    return messageSPhraseAdd        

def checkQuantityRoleStation(checkRoleStation: list, role: str):
    """
    Считает кол-во станций с заданой ролью
    """
    quantity = 0
    for i in checkRoleStation:
        if i[:1] == role:
            quantity += 1
    return quantity

def checkLogicalMessage(numberStation, resultCheckFormat):
    """
    Логический контроль сообщения
    """
         
    global numberErrors
    global stopCheck
    global stationsPassedThrough # Список станций, по которым продвигаются поезда
    global skipCheck

    def differenceTime(hoursStart:int, minutesStart:int, hoursStop:int, minutesStop:int):
        """
        Расчет разницы в часах и минутах между двумя моментами времени в сообщениях
        """

        if minutesStart <= minutesStop:
            differenceMinutes = minutesStop - minutesStart
        else:
            hoursStop = hoursStop - 1
            differenceMinutes = 60 + minutesStop - minutesStart
        if hoursStart <= hoursStop:
            differenceHours = hoursStop - hoursStart
        else:
            differenceHours = 24 + hoursStop - hoursStart
        return differenceHours, differenceMinutes
    
    # проверка последовательности сообщений
    if listMessages[-1][0] == '200' and numberStation > 1 and listMessages[-2][0] != '205' and listMessages[-1][1] == listMessages[-2][1]:
        numberErrors += 1
        fileTXTResult.write('Нарушена очередность передачи сообщения 200. Отсутствует сообщение 205. Ошибка '+ str(numberErrors)+'\n')
        skipCheck +=1
    elif listMessages[-1][0] == '202' and numberStation > 1 and (listMessages[-2][0] != '200' and listMessages[-2][0] != '202'):
        numberErrors += 1
        fileTXTResult.write('Нарушена очередность передачи сообщения 202. Отсутствует сообщение 200 или 202. Ошибка '+ str(numberErrors)+'\n')
        skipCheck +=1
    elif listMessages[-1][0] == '201' and numberStation > 1 and (listMessages[-2][0] != '200' and listMessages[-2][0] != '202'):
        numberErrors += 1
        skipCheck +=1
        fileTXTResult.write('Нарушена очередность передачи сообщения 201. Отсутствует сообщение 200 или 202. Ошибка '+ str(numberErrors)+'\n')
    elif listMessages[-1][0] == '205' and numberStation > 1 and (listMessages[-2][0] != '201') and listMessages[-2][1] == listMessages[-1][1]:
        numberErrors += 1
        skipCheck +=1
        fileTXTResult.write('Нарушена очередность передачи сообщения 205. Отсутствует сообщение 201. Ошибка '+ str(numberErrors)+'\n')
    elif listMessages[-1][0] == '203' and numberStation > 1 and (listMessages[-2][0] != '201') and listMessages[-2][1] == listMessages[-1][1]:
        numberErrors += 1
        skipCheck +=1
        fileTXTResult.write('Нарушена очередность передачи сообщения 205. Отсутствует сообщение 201. Ошибка '+ str(numberErrors)+'\n')
    

    # проверка на присутствие станции передачи сообщения в списке станций
    if listMessages[-1][1][:4] not in set(stations[0]):
        numberErrors += 1
        fileTXTResult.write('Станция '+ listMessages[-1][1][:4] + ' отсутствует в маршруте движения поезда. Ошибка ' + str(numberErrors) + '. Проверка прервана \n')
        skipCheck += 1
        return numberStation
    
    # Проверка перехода поезда на следующую станцию
    if ((listMessages[-1][0] == '202' or (listMessages[-1][0] == '205' and numberStation == 0 )  
        or (listMessages[-1][0] == '201' and numberStation != 0)) and listMessages[-1][1] not in set(stationsPassedThrough)): 
            stationsPassedThrough.append(listMessages[-1][1])
            numberStation += 1
    elif listMessages[-1][0] == '200' and numberStation == 0:
        numberErrors += 1
        fileTXTResult.write('\t\t Сообщение 200 не может быть первым сообщением о движении поезда. Ошибка '+ str(numberErrors)+'\n')
        skipCheck +=1

    elif ((listMessages[-1][0] == '202' or (listMessages[-1][0] == '205' and numberStation == 0 )  
            or (listMessages[-1][0] == '201' and numberStation > 1)) and listMessages[-1][1] in set(stationsPassedThrough)):
        numberErrors += 1
        skipCheck +=1
        fileTXTResult.write('\t\t Через станцию '+ listMessages[-1][1][:4] + ' поезд уже проезжал. Проверка следующих сообщений пропущена. Ошибка '+ str(numberErrors)+'\n')
    

    if resultCheckFormat == 'ОШИБКА МАКЕТА СООБЩЕНИЯ':
        numberErrors += 1
        fileTXTResult.write('\t\t Логическая проверка сообщения пропущена. Ошибка '+ str(numberErrors)+'\n')
        return numberStation
    
    if skipCheck == 0:    
        if ((listMessages[-1][0] != '202' or listMessages[-1][0] != '205') and numberStation == 0 and len(listMessages) == 1):
            numberErrors += 1
            fileTXTResult.write('\t\t Это сообщение не может быть первым. Ошибка '+ str(numberErrors)+'\n')
            
        if listMessages[-1][1] != '0000':
            if ((listMessages[-1][1] !=  stations[0][numberStation-1] and len(listMessages[-1][1]) == 4) 
                or (listMessages[-1][1][-4:] !=  stations[0][numberStation-1] and len(listMessages[-1][1]) == 9  
                and stations[1][stations[0].index(listMessages[-1][3])][:1] == '3' 
                and stations[1][stations[0].index(listMessages[-1][5])][:1] == '3' 
                and (listMessages[-1][0] == '201' or listMessages[-1][0] == '203'))): # проверка станции передачи сообщения
                numberErrors += 1
                fileTXTResult.write(listMessages[-1][1] + ' Станция передачи сообщение НЕ СООТВЕТСТВУЕТ маршруту следования. Ошибка '+ str(numberErrors)+'\n')
            else: 
                pass
                if flagLoging == 1:
                    fileTXTResult.write(stations[0][numberStation-1] + ' Станция передачи сообщение соответствует маршруту следования\n')
        else:
            numberErrors += 1
            fileTXTResult.write('ОШИБКА МАКЕТА. Код ЕСР станции не проверяется. Ошибка '+ str(numberErrors)+'\n')
        
        # ! для поездов между двумя станциями проверка соответствия станции формирования и станции отправления с первой станции
        if len(stations[0]) == 2 and listMessages[-1][1][:4] == listMessages[-1][3]:
            if flagLoging == 1:
                fileTXTResult.write('\t\tСтанция '+ listMessages[-1][1][:4] + ' передачи сообщения соотвествует станции формирования поезда\n')
        elif len(stations[0]) == 2 and listMessages[-1][1][:4] != listMessages[-1][3] and (listMessages[-1][1] == '205' and listMessages[-1][1] == '200'):
            numberErrors += 1
            fileTXTResult.write('\t\tСтанция '+ listMessages[-1][1][:4] + ' передачи сообщения НЕ СООТВЕСТВУЕТ станции '+ listMessages[-1][3] +  ' формирования поезда. Ошибка '+ str(numberErrors)+
            '\n\t\t Проверка следующих сообщений не выполняется. \n' )
            skipCheck += 1
            return(numberStation)
        
        
        # ! для поездов между двумя станциями проверка соответствия индекса поезда станциям начала и окончания движения поезда
        if len(stations[0]) == 2 and stations[0][0] == listMessages[-1][3] and stations[0][1] == listMessages[-1][5]:
            if flagLoging == 1:
                fileTXTResult.write('\t\tСтанция формирования '+ listMessages[-1][3] + ' соответствует станции ' + stations[0][0]+' начала движения поезда.\n')
                fileTXTResult.write('\t\tСтанция назначения '+ listMessages[-1][5] + ' соответствует станции ' + stations[0][1] + ' окончания движения поезда.\n')
        elif len(stations[0]) == 2 and stations[0][0] != listMessages[-1][3]:
            numberErrors += 1
            fileTXTResult.write('\t\tСтанция формирования '+ listMessages[-1][3] + ' НЕ СООТВЕТСТВУЕТ станции ' + stations[0][0]+' начала движения поезда. Ошибка '+ str(numberErrors)+'\n')
            skipCheck += 1
            return(numberStation)
        elif len(stations[0]) == 2 and stations[0][0] != listMessages[-1][3]:
            numberErrors += 1
            fileTXTResult.write('\t\tСтанция назначения '+ listMessages[-1][5] + ' НЕ СООТВЕТСТВУЕТ станции ' + stations[0][1] + ' окончания движения поезда. Ошибка '+ str(numberErrors)+'\n')
            skipCheck += 1
            return(numberStation)
        
        
        if (len(stations[0]) == 2 and listMessages[-1][1][-4:] ==  stations[0][numberStation-1] and len(listMessages[-1][1]) == 9  
                and (stations[1][stations[0].index(listMessages[-1][3])][:1] == '3' or stations[1][stations[0].index(listMessages[-1][3])][:1] == '1') 
                and stations[1][stations[0].index(listMessages[-1][5])][:1] == '3' 
                and (listMessages[-1][0] == '201' or listMessages[-1][0] == '203')):
            pass
            if flagLoging == 1:
                    fileTXTResult.write('Станция '+ listMessages[-1][3] + '  передает сообщение за станцию ' + stations[0][numberStation-1] +'\n')
        elif (len(stations[0]) == 2 and listMessages[-1][1][-4:] ==  stations[0][numberStation-1] and len(listMessages[-1][1]) != 9  
                and stations[1][stations[0].index(listMessages[-1][3])][:1] == '3' 
                and stations[1][stations[0].index(listMessages[-1][5])][:1] == '3' 
                and (listMessages[-1][0] == '201' or listMessages[-1][0] == '203')):
            numberErrors += 1
            fileTXTResult.write('Станция '+ listMessages[-1][3] + '  должна передать сообщение за станцию ' + stations[0][numberStation-1] +'. Ошибка '+ str(numberErrors)+'\n')
        
        
        
        # проверка соответствия роли станции передаваемым сообщениям
        if (listMessages[-1][0] == '202' and stations[1][stations[0].index(listMessages[-1][1])][:1] not in listRole202):
            numberErrors += 1
            fileTXTResult.write('\t Стания ' + listMessages[-1][1]+ ' не может передавать сообщение о проследовании. Ошибка '+ str(numberErrors)+'\n')
        elif ((listMessages[-1][0] == '200' or listMessages[-1][0] == '201' or listMessages[-1][0] == '205' or listMessages[-1][0] == '203')
            and stations[1][stations[0].index(listMessages[-1][1][:4])][:1] not in listRole200):
            numberErrors += 1
            fileTXTResult.write('\t Стания ' + listMessages[-1][1]+ ' не может передавать сообщение о работе с поездом на станции. Ошибка '+ str(numberErrors)+'\n')
            
        # проверка номера поезда через кол-во технических станций и междор стыков в маршруте
        if numberStation == 1: # Если станция первая в списке, проверяем соответствие номера сквозному
            if (listMessages[-1][2][:1] == '2' and quantityTechnStation >= 3  # кол-во сорт и участ ст-ий >= 3
                                            and quantityBoardStation == 0  # кол-во междор стыков нет
                                        or (quantityTechnStation >=2 # кол-во сорт и участ ст-ий >= 2
                                            and quantityBoardStation > 0)): # кол-во междор стыков > 0
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t\t Кол-во техн станций на маршруте движения ' + str(quantityTechnStation) +
                                    ', кол-во междор стыков ' + str(quantityBoardStation) +' поезд сквозной ' + listMessages[-1][2] +'\n')
            else:
                if flagLoging == 1:
                    fileTXTResult.write('\t\t Кол-во техн станций на маршруте движения ' + str(quantityTechnStation) +
                                    ', кол-во междор стыков ' + str(quantityBoardStation) +' поезд не сквозной ' + listMessages[-1][2] + '\n')
        else:
            if numberStation > 0:    
                if (listMessages[-2][2] == listMessages[-1][2]
                    or int(listMessages[-2][2]) == int(listMessages[-1][2])+1
                    or int(listMessages[-2][2]) == int(listMessages[-1][2])-1):
                    pass
                    if flagLoging == 1:
                        fileTXTResult.write('\t\t Номер поезда соответствует предыдущему сообщению\n')
                else:
                    numberErrors += 1
                    fileTXTResult.write('\t\t Номер поезда НЕ СООТВЕТСТВУЕТ предыдущему сообщению. Ошибка '+ str(numberErrors)+'\n')
            else: 
                pass # fileTXTResult.write('\t\t Это сообщение не может быть первым\n')

        # проверка номера поезда при движении между двумя станциями
        if len(stations[0]) == 2 and (listMessages[-1][2][:2] == '36' or listMessages[-1][2][:2] == '35'):
            if flagLoging == 1:
                    fileTXTResult.write('\t\t Номер поезда ' + listMessages[-1][2] + ' соответствует маршруту его движения\n')
        elif len(stations[0]) == 2 and (listMessages[-1][2][:2] != '36' and listMessages[-1][2][:2] != '35'):
            numberErrors += 1
            fileTXTResult.write('\t\t Номер поезда ' + listMessages[-1][2] + ' НЕ СООТВЕТСТВУЕТ маршруту его движения. Ошибка '+ str(numberErrors)+'\n')

        if numberStation == 1 and len(stations[0]) == 2 and listMessages[-1][1][:4] != listMessages[-1][3]:
            numberErrors += 1
            fileTXTResult.write('\t\t Индекс поезда  НЕ СООТВЕСТВУЕТ СТАНЦИИ ФОРМИРОВАНИЯ. Ошибка '+ str(numberErrors)+'\n')

        if numberStation == 2 and len(stations[0]) == 2 and listMessages[-1][1][-4:] != listMessages[-1][5]:
            numberErrors += 1
            fileTXTResult.write('\t\t Индекс поезда  НЕ СООТВЕСТВУЕТ СТАНЦИИ НАЗНАЧЕНИЯ. Ошибка '+ str(numberErrors)+'\n')

        # проверка индекса поезда

        if numberStation == 1:
            if listMessages[-1][2][:1] == '2' and ((listMessages[-1][3][:2] not in setRegions and listMessages[-1][5][:2] not in setRegions) # ст-ии форм-ия и назн-ия не входят в дорогу 
                or (listMessages[-1][3][:2] not in setRegions and listMessages[-1][5][:2] in setRegions) # ст-ия форм-ия не входит в дорогу, ст-ия назн-ия входит
                or (listMessages[-1][3][:2] in setRegions and listMessages[-1][5][:2] not in setRegions) # ст-ии форм-ия входит в дорогу и ст-ия назн-ия не входят в дорогу 
                or (listMessages[-1][3][:2] in setRegions and listMessages[-1][5][:2] in setRegions  # ст-ии форм-ия и назн-ия входят в дорогу 
                    and listMessages[-1][3][:2] != listMessages[-1][5][:2])):
                if flagLoging == 1:
                    fileTXTResult.write('\t\t Индекс поезда соответствует номеру поезда\n')
            
            elif listMessages[-1][2][:1] == '3' and (listMessages[-1][3][:2] in setRegions and listMessages[-1][3][:2] == listMessages[-1][5][:2]):
                if flagLoging == 1:
                    fileTXTResult.write('\t\t Номер поезда соответствует индексу поезда\n')
                
            
            else:
                numberErrors += 1
                fileTXTResult.write('\t\t Номер поезда НЕ СООТВЕТСТВУЕТ индексу поезда. Ошибка '+ str(numberErrors)+'\n')    
            
            if (listMessages[-1][3] in stationsAllSet and
                stationsAllList[1][stationsAllList[0].index(listMessages[-1][3])][:1] not in listRole200):
                numberErrors += 1
                fileTXTResult.write('\t\tСтанция ' + listMessages[-1][3] + ' НЕ МОЖЕТ  быть станцией формирования поезда. Ошибка '+ str(numberErrors)+'\n')
            
            if (listMessages[-1][5] in stationsAllSet and
                stationsAllList[1][stationsAllList[0].index(listMessages[-1][5])][:1] not in listRole200) :
                numberErrors += 1
                fileTXTResult.write('\t\tСтанция ' + listMessages[-1][5] + ' НЕ МОЖЕТ быть станцией назначения поезда. Ошибка '+ str(numberErrors)+'\n')
                
        if numberStation > 1:
            if compareField(3)==1 and compareField(4)==1 and compareField(5)==1:
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t\t Индекс поезда соответствует индексу поезда в предыдущем сообщении\n')
            else:
                numberErrors += 1
                fileTXTResult.write('\t\t Индекс поезда НЕ СООТВЕТСТВУЕТ индексу поезда в предыдущем сообщении. Ошибка '+ str(numberErrors)+'\n')
        
        # проверка направления движения
        # соответствие длины поля направления в с.202 для узловых станций
        if (listMessages[-1][0] == '202' and (stations[1][stations[0].index(listMessages[-1][1])][:1] != '4' and stations[1][stations[0].index(listMessages[-1][1])][:1] != '3')
                and len(listMessages[-1][6]) != 4  ):
            numberErrors += 1
            fileTXTResult.write('\t\t Станцция ' + listMessages[-1][1] + ' НЕ ЯВЛЯЕТСЯ ПРОМЕЖУТОЧНОЙ УЗЛОВОЙ. Указывается только направление ОТКУДА. Ошибка '+ str(numberErrors)+'\n')
        elif (listMessages[-1][0] == '202' and (stations[1][stations[0].index(listMessages[-1][1])][:1] == '4'
                                            or stations[1][stations[0].index(listMessages[-1][1])] == '31')
                and len(listMessages[-1][6]) != 4  ):
            pass
            if flagLoging == 1:
                fileTXTResult.write('\t\t Станцция ' + listMessages[-1][1] + ' узловая \n')
        
        # с. 205 и 200
        if listMessages[-1][0] == '205' or listMessages[-1][0] == '200':
                codeStationWhere = findCodeStThroughRoleWhere(listMessages[-1][6])
                if listMessages[-1][6] == codeStationWhere or listMessages[-1][6][:2] not in setRegions:
                    pass
                    if flagLoging == 1:
                        fileTXTResult.write('\t\t' + listMessages[-1][6] + ' Напр. следования поезда КУДА соответствует маршруту\n')
                else:
                    numberErrors += 1
                    fileTXTResult.write('\t\t' + listMessages[-1][6] + ' Напр. следования поезда КУДА НЕ СООТВЕТСТВУЕТ маршруту. Ошибка '+ str(numberErrors)+'\n')
        
        # с. 201
        elif listMessages[-1][0] == '201': 
            codeStationWhereFrom = findCodeStThroughRoleWhereFrom(listMessages[-1][6]) 
            if listMessages[-1][6] == codeStationWhereFrom or listMessages[-1][6][:2] not in setRegions:
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t\t' + listMessages[-1][6] + ' Напр. следования поезда ОТКУДА соответствует маршруту\n')
            else:
                numberErrors += 1
                fileTXTResult.write('\t\t' + listMessages[-1][6] + ' Напр. следования поезда ОТКУДА НЕ СООТВЕТСТВУЕТ маршруту. Ошибка '+ str(numberErrors)+'\n')
        
        # с. 202
        elif listMessages[-1][0] == '202': 
            if numberStation >= 1: # сообщение первое и далее в описании движения поезда
                if listMessages[-1][6][:2] not in setRegions:
                    pass
                    if flagLoging == 1:
                        fileTXTResult.write('\t\t' + listMessages[-1][6] + ' Напр. следования поезда ОТКУДА соответствует маршруту\n')
                elif listMessages[-1][6][:4] != findCodeStThroughRoleWhereFrom(listMessages[-1][6][:4]):
                    numberErrors += 1
                    fileTXTResult.write('\t\t' + listMessages[-1][6] + ' Напр. следования поезда ОТКУДА НЕ СООТВЕТСТВУЕТ маршруту. Ошибка '+ str(numberErrors)+'\n')
                
            elif numberStation > 1:
                # if (listMessages[-1][0] == '201'): # вынести 201 сообщение отдельно
                codeStationWhereFrom = findCodeStThroughRoleWhereFrom(listMessages[-1][6][:4])
                if listMessages[-1][6][:4] == codeStationWhereFrom:
                    pass
                    if flagLoging == 1:
                        fileTXTResult.write('\t\t' + listMessages[-1][6][:4] + ' Напр. следования поезда ОТКУДА соответствует маршруту\n')
                else:
                    numberErrors += 1
                    fileTXTResult.write('\t\t' + listMessages[-1][6][:4] + ' Напр. следования поезда ОТКУДА НЕ СООТВЕТСТВУЕТ маршруту. Ошибка '+ str(numberErrors)+'\n')
                if stations[1][stations[0].index(listMessages[-1][1])][:1] == '4':
                    codeStationWhere = findCodeStThroughRoleWhere(listMessages[-1][6][5:])
                    if listMessages[-1][6][5:] == findCodeStThroughRoleWhereFrom(listMessages[-1][6][5:]):
                        pass
                        if flagLoging == 1:
                            fileTXTResult.write('\t\t' + listMessages[-1][6][5:] + ' Напр. следования поезда КУДА соответствует маршруту\n')
                    else:
                        numberErrors += 1
                        fileTXTResult.write('\t\t' + listMessages[-1][6][5:] + ' Напр. следования поезда КУДА НЕ СООТВЕТСТВУЕТ маршруту. Ошибка '+ str(numberErrors)+'\n')
                
        elif listMessages[-1][0] == '203':
            if len(listMessages[-1][6]) == 8:
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t\t № вагона из восьми цифр\n')
            else:
                numberErrors += 1
                fileTXTResult.write('\t\t № вагона должен быть из восьми цифр. Ошибка '+ str(numberErrors)+'\n')
                
        else:
            fileTXTResult.write('\t\t Напр. следования поезда не проверялось\n')

        # проверка даты и времени
        # daysOperation = int(listMessages[-1][7])
        # monthsOperation = int(listMessages[-1][8])
        hoursOperation = int(listMessages[-1][9])
        minutesOperation = int(listMessages[-1][10])
        # проверка простоя на сорт. станции
        if listMessages[-1][0] == '205' and numberStation != 1 and listMessages[-2][0] == '201' and stations[1][stations[0].index(listMessages[-1][1])][:1] == '1':
            hoursParking, minutesParking = differenceTime(int(listMessages[-2][9]),int(listMessages[-2][10]),hoursOperation,minutesOperation) 
            if hoursParking*60+minutesParking < 40:
                numberErrors += 1
                fileTXTResult.write('\t\t ' + str(hoursParking*60+minutesParking) + ' мин. Время стоянки поезда на сорт. станции меньше 40 минут. Ошибка '+ str(numberErrors)+'\n')
            else:
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t\t ' + str(hoursParking*60+minutesParking) + ' Время стоянки поезда на сорт. станции \n')
        
        # проверка простоя на участ. станции от прибытия до готовности к отправлению
        if listMessages[-1][0] == '205' and numberStation != 1 and listMessages[-2][0] == '201' and stations[1][stations[0].index(listMessages[-1][1])][:1] == '2':
            hoursParking, minutesParking = differenceTime(int(listMessages[-2][9]),int(listMessages[-2][10]),hoursOperation,minutesOperation) 
            if hoursParking*60+minutesParking < 15:
                numberErrors += 1
                fileTXTResult.write('\t\t ' + str(hoursParking*60+minutesParking) + ' Время стоянки поезда на участ. станции меньше 15 минут. Ошибка '+ str(numberErrors)+'\n')
            else:
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t\t ' + str(hoursParking*60+minutesParking) + ' Время стоянки поезда на участ. станции \n')
        
        # проверка простоя на сорт. и участ. станциях от с.205 до с.200
        if numberStation > 1 and listMessages[-1][0] == '200' and listMessages[-2][0] == '205': # and (stations[1][stations[0].index(listMessages[-1][1])][:1] == '2'):
            hoursParking, minutesParking = differenceTime(int(listMessages[-2][9]),int(listMessages[-2][10]),hoursOperation,minutesOperation) 
            if hoursParking*60+minutesParking > 10:
                numberErrors += 1
                fileTXTResult.write('\t\t ' + str(hoursParking*60+minutesParking) + ' мин. Время стоянки поезда от готовности до отправления больше 10 минут. Ошибка '+ str(numberErrors)+'\n')
            else:
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t\t ' + str(hoursParking*60+minutesParking) + ' Время стоянки поезда от готовности до отправления\n')

        # проверка простоя на сорт. станции от с.201 до с.203
        if listMessages[-1][0] == '203' and numberStation != 1 and listMessages[-2][0] == '201': # and stations[1][stations[0].index(listMessages[-1][1])][:1] == '2':
            hoursParking, minutesParking = differenceTime(int(listMessages[-2][9]),int(listMessages[-2][10]),hoursOperation,minutesOperation) 
            if hoursParking*60+minutesParking < 15:
                numberErrors += 1
                fileTXTResult.write('\t\t ' + str(hoursParking*60+minutesParking) + ' мин. Время стоянки поезда от прибытия до расформирования меньше 15 минут. Ошибка '+ str(numberErrors)+'\n')
            else:
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t\t ' + str(hoursParking*60+minutesParking) + ' мин. Время стоянки поезда от прибытия до расформирования\n')
        
        # проверка времени от явки до с.205 на сорт. и учат. станциях
        if listMessages[-1][0] == '205' and numberStation != 1 and listMessages[-2][0] == '201' and stations[1][stations[0].index(listMessages[-1][1])][:1] == '2':
            hoursParkingBrigade, minutesParkingBrigade = differenceTime(int(listMessages[-1][16]),int(listMessages[-1][17]),hoursOperation,minutesOperation) 
            if hoursParkingBrigade*60+minutesParkingBrigade > 120:
                numberErrors += 1
                fileTXTResult.write('\t\t ' + str(hoursParkingBrigade*60+minutesParkingBrigade) + ' мин. Время работы лок. бригады до готовности больше 120 минут. Ошибка '+ str(numberErrors)+'\n')
            else:
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t\t ' + str(hoursParkingBrigade*60+minutesParkingBrigade) + ' мин. Время работы лок. бригады до готовности\n')
        
        pass


        # проверка работы с локомотивом
        pass
        if listMessages[-1][0] != '203':
            # проверка серии локомотива и номера лок-ва
            if numberStation != 1 and listMessages[-1][0] == '205' and listMessages[-2][12] == '1' and compareField(13) == 0 and compareField(14) == 0:
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t Смена лок-ва выполнена\n')
            elif numberStation > 1 and listMessages[-1][0] == '205' and listMessages[-2][12] == '1' and compareField(14) == 1:
                numberErrors += 1
                fileTXTResult.write('\t Смена лок-ва НЕ ВЫПОЛНЕНА. ОШИБКА ' + str(numberErrors) + '\n')
            elif numberStation != 1 and listMessages[-1][0] == '205' and listMessages[-2][12] == '0': #  and compareField(14) == 1:
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t Смена лок-ва не нужна\n')    
            pass
            # проверка номера лок-ва
            if numberStation == 1 and (listMessages[-1][0] == '202' or listMessages[-1][0] == '205' or listMessages[-1][0] == '200'):
                if listMessages[-1][14][:-1] == '0000':
                    numberErrors += 1
                    fileTXTResult.write('\t Номер лок-ва '+ listMessages[-1][14] + ' НЕ ДОПУСТИМ. ОШИБКА ' + str(numberErrors) + '\n')
                if listMessages[-1][14][-1:] == '0' or listMessages[-1][14][-1:] == '1' or listMessages[-1][14][-1:] == '2':
                    pass
                    if flagLoging == 1:
                        fileTXTResult.write('\t Номер лок-ва допустим\n')
                else:
                    numberErrors += 1
                    fileTXTResult.write('\t\t Последний символ № лок-ва НЕ ВЕРЕН. Ошибка '+ str(numberErrors)+'\n')
            elif (numberStation > 1 and (listMessages[-1][0] == '202' or listMessages[-1][0] == '200' 
                                        or listMessages[-1][0] == '201' 
                                        or (listMessages[-1][0] == '205' and listMessages[-2][11] == '0')) 
                                    and compareField(13) == 1 and compareField(14) == 1):
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t Серия и Номер лок-ва соответствует предыдущему сообщенияю\n')
            elif (numberStation != 1 and listMessages[-1][0] == '205' and listMessages[-2][11] == '1'
                and compareField(13) == 0 and (listMessages[-1][13][-1:] == '0' or listMessages[-1][13][-1:] == '1' 
                                                or listMessages[-1][13][-1:] == '2')):
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t Смена лок-ва. Номер лок-ва допустим\n')
            
            # проверка вида слелования лок-ва
            if listMessages[-1][15] == '1':
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t '+ listMessages[-1][15] + ' Вид следования лок-ва соответствует <<В ГОЛОВЕ>> \n')
            else:
                numberErrors += 1
                fileTXTResult.write('\t '+ listMessages[-1][15] + ' Вид следования лок-ва  НЕ СООТВЕТСТВУЕТ <<В ГОЛОВЕ>>. Ошибка '+ str(numberErrors)+'\n')

            # проверка времени работы лок-ой бригады
            hoursBrigade = int(listMessages[-1][16])
            minutesBrigade = int(listMessages[-1][17])
            
            hoursWork, minutesWork = differenceTime(hoursBrigade,  minutesBrigade, hoursOperation, minutesOperation)

            if hoursWork <= 12:
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t ' + str(hoursWork)+ ' ' +str(minutesWork) + ' Время работы лок. бригады не превышает 12 часов \n')
            else:
                numberErrors += 1
                fileTXTResult.write('\t ' + str(hoursWork)+ ' час. ' +str(minutesWork) + ' мин. Время работы лок. бригады ПРЕВЫШАЕТ 12 ЧАСОВ. Ошибка '+ str(numberErrors)+'\n')

            # проверка депо приписки
            if listMessages[-1][18][-2:] != '00':
                if flagLoging == 1:
                    fileTXTResult.write('\t ' + listMessages[-1][18] + ' Номер депо приписки лок. бригады допустим \n')
            else:
                numberErrors += 1
                fileTXTResult.write('\t ' + listMessages[-1][18] + ' Номер депо приписки лок. бригады НЕ ДОПУСТИМ. Ошибка '+ str(numberErrors)+'\n')

            if numberStation == 1:
                if listMessages[-1][0] == '202' and stations[1][stations[0].index(listMessages[-1][1])][:1] == '5':
                    if listMessages[-1][18][:2] == min(list(setRegions)):
                        pass
                        if flagLoging == 1:
                            fileTXTResult.write('\t ' + listMessages[-1][18] + ' Депо приписки лок. бригады заданной дороги \n')
                    elif listMessages[-1][18][:2] not in setRegions:
                        pass
                        if flagLoging == 1:
                            fileTXTResult.write('\t ' + listMessages[-1][18] + ' Депо приписки лок. бригады не заданной дороги \n')
                    else:
                        numberErrors += 1
                        fileTXTResult.write('\t ' + listMessages[-1][18] + ' Депо приписки лок. бригады НЕ СООТВЕТСВУЕТ заданой дороге. Ошибка '+ str(numberErrors)+'\n')
                elif listMessages[-1][0] == '205':
                    if listMessages[-1][18][:2] == min(list(setRegions)):
                        pass
                        if flagLoging == 1:
                            fileTXTResult.write('\t ' + listMessages[-1][18] + ' Депо приписки лок. бригады заданной дороги \n')
                    else:
                        numberErrors += 1
                        fileTXTResult.write('\t ' + listMessages[-1][18] + ' Депо приписки лок. бригады НЕ СООТВЕТСВУЕТ заданой дороге. Ошибка '+ str(numberErrors)+'\n')
            else:
                if numberStation > 1 and (listMessages[-1][0] == '202' or listMessages[-1][0] == '201' or listMessages[-1][0] == '200') and compareField(18) == 1:
                    pass
                    if flagLoging == 1:
                        fileTXTResult.write('\t ' + listMessages[-1][18] + ' Депо приписки лок. бригады СООТВЕТСВУЕТ предыдущему сообщению \n')
                elif listMessages[-1][0] == '205' and listMessages[-2][0] == '201' and listMessages[-1][18][:2] == min(list(setRegions)):
                    pass
                    if flagLoging == 1:
                        fileTXTResult.write('\t ' + listMessages[-1][18] + ' Депо приписки лок. бригады нашего региона \n')
                elif listMessages[-1][0] == '205' and listMessages[-2][0] == '201' and listMessages[-1][18][:2] != min(list(setRegions)):
                    numberErrors += 1
                    fileTXTResult.write('\t ' + listMessages[-1][18] + ' Депо приписки лок. бригады НЕ СООТВЕТСТВЕТ заданной дороге. Ошибка '+ str(numberErrors)+'\n')
                else:
                    numberErrors += 1
                    fileTXTResult.write('\t ' + listMessages[-1][18] + ' Депо приписки лок. бригады НЕ СООТВЕТСВУЕТ ' + listMessages[-2][18] + ' предыдущему сообщению. Ошибка '+ str(numberErrors)+'\n\n')
                            

            # проверка табельного номера лок-ой бригады и фамилии машиниста
            if (listMessages[-1][0] == '205' and numberStation != 1 and stations[1][stations[0].index(listMessages[-1][1])][:1] == '1'
                and stations[1][stations[0].index(listMessages[-1][1])][:1] == '2' and compareField(19) == 0 and compareField(20) == 0):
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t ' + listMessages[-1][19] + listMessages[-1][20] + ' Смена лок. бригады выполнена \n')
            elif ((listMessages[-1][0] != '205' and listMessages[-1][0] != '203' )and numberStation != 1 
                and compareField(19) == 1 and compareField(20) == 1):
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t ' + listMessages[-1][19] + ' ' + listMessages[-1][20] + ' Лок. бригада соответствует предыдущему сообщению\n')
            elif (listMessages[-1][0] == '205' and numberStation > 1 
                and (compareField(19) == 0 or compareField(20) == 0)):
                pass
                if flagLoging == 1:
                    fileTXTResult.write('\t ' + listMessages[-1][19] + ' ' + listMessages[-1][20] + ' Лок. бригада сменена\n')
            
            elif ((listMessages[-1][0] != '205' or listMessages[-1][0] != '203' ) and numberStation > 1
                and (compareField(19) == 0 or compareField(20) == 0)):
                numberErrors += 1
                fileTXTResult.write('\t ' + listMessages[-1][19] + ' ' + listMessages[-1][20] + 
                                    ' Лок. бригада НЕ СООТВЕТСТВУЕТ ' + listMessages[-2][19] + ' ' + listMessages[-2][20] 
                                    + ' предыдущему сообщению. Ошибка '+ str(numberErrors)+'\n')

    skipCheck = 0
    return numberStation


def findCodeStThroughRoleWhere(codeSt):
    """
    Поиск кода ЕСР станции направления движения "КУДА" 
    """
    if codeSt in stations[0]:
        stationIndex = stations[0].index(codeSt) # определяю индекс станции в списке станций
        for role in stations[1][stationIndex+1:]: # двигаюсь по списку ролей станций от позиции станции до конца списка
            if role[:1] == '1' or role[:1] == '2': # нашли роль техн. станции
                roleIndex = stations[1].index(role) # определяем индекс роли в списке
                technStation = stations[0][roleIndex] # определяем код ЕСР станции по индексу роли в списке
                break
            elif role[:1] == '5': # 
                technStation = '0000'
                break
            elif role[:1] == '3': # 
                technStation = codeSt
                break
        technStation = codeSt
    else:
        technStation = '0000'
        pass
    return technStation

def findCodeStThroughRoleWhereFrom(codeSt):
    """
    Поиск кода ЕСР станции направления движения "ОТКУДА" 
    """
    if codeSt in stations[0]:
        stationIndex = stations[0].index(codeSt)
        for pozition in range(stationIndex-1, -1, -1): # двигаюсь по списку ролей станций от позиции станции до начала списка
            if stations[1][pozition][:1] == '1' or stations[1][pozition][:1] == '2': # нашли роль техн. станции
                roleIndex = stations[1].index(stations[1][pozition]) # определяем индекс роли в списке
                technStation = stations[0][roleIndex] # определяем код ЕСР станции по индексу роли в списке
                break
            
            """ elif stations[1][pozition][:1] == '5': # 
                technStation = '0000'
                break
            elif stations[1][pozition][:1] == '3': # 
                technStation = codeSt
                break """
        technStation = codeSt
    else:
        technStation = '0000'
    return technStation
 
def compareField(numberField:int):
    """
    Сравнение поля с номером numberField последней и предпоследней записей в списке сообщений
    """
    if listMessages[-2][numberField] != listMessages[-1][numberField]:
        return 0
    return 1
 # -----------------------------------------------------------------------------------------------------   
# os.chdir('Для проверки//')
pathForCheck = 'Для проверки//' # папка хранения проверяемых файлов
pathPastCheck = 'После проверки//' # папка хранения результатов проверки
numberErrors = 0 
dictStation = dict()
stations = list()
setRegions = set()
messageSPhrase = list()
messageIPhrase = list()

messageIPhraseEmpty = ['000','00000','0','00','00','0000','00000','00']
message = list()
messageTemp = list()
listMessages = list()
roleStations = list()
listRole202 = ['3', '4', '5', '6'] # начало кодов ролей станций отправляющие с.202
listRole200 = ['3', '1', '2'] # начало кодов ролей станций отправляющие с.200
stopCheck = 0 # Для остановки проверки файла при критических ошибках
stationsPassedThrough = list() # для контроля за проследованием станций
skipCheck = 0

def detect_encoding(file_path):
    with fileTXT as file: #open(file_path, 'rb') as file:
        detector = chardet.universaldetector.UniversalDetector()
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result['encoding']

fileList = os.listdir(pathForCheck) 
for nameFileTXT in fileList:
    if nameFileTXT[-3:] != 'txt': # открываем файлы только с расширением TXT
        continue
    else:
        numberErrors = 0
        stopCheck = 0
        fileTXT = open(pathForCheck+nameFileTXT, 'rb') # открытие проверяемого файла 
        encodingFileTXT = detect_encoding(fileTXT)
        fileTXT = open(pathForCheck+nameFileTXT, 'r', encoding = str(encodingFileTXT))
        nameFileTXTResult = pathPastCheck+nameFileTXT[0:len(nameFileTXT)-4]+'_result'+'.txt'
        fileTXTResult = open(nameFileTXTResult, 'w', encoding = 'utf-8') # результат проверки, encoding='cp1251'
        # обработка номеров вагонов
        for i in fileTXT:
            lineTXT = i.strip()
            if len(lineTXT) != 8 and lineTXT != '' and lineTXT != '#':
                numberErrors += 1
                fileTXTResult.write(lineTXT + ' не является номером вагона. Нарушен формат файла. Проверка прервана. Ошибка '+ str(numberErrors)+'\n')
                stopCheck += 1
                break
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
        setRegions.clear()
        for i in fileTXT:
            if stopCheck != 0:
                break
            lineTXT = i.strip()
            if lineTXT == '':
                continue
            elif lineTXT == '#':
                break
            elif len(lineTXT) != 9:
                numberErrors += 1
                fileTXTResult.write(lineTXT + ' Формат строки НЕ ВЕРЕН. Проверка прервана. Ошибка '+ str(numberErrors)+'\n')
                stopCheck += 1
                break
            else:
                dictStation[lineTXT[3:7]] = lineTXT[:2]
                if len(dictStation) == 1:
                    setStation = {lineTXT[3:7]}
                    setRegions =  {lineTXT[3:7][:2]}
                else:
                    setStation.add(lineTXT[3:7])
                    setRegions.add(lineTXT[3:7][:2])
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
        stationsAllList = list()
        stationsAllList.append(list(dictStation.keys()))
        stationsAllList.append(list(dictStation.values()))
        stationsAllSet = set(list(dictStation.keys()))
        fileTXTResult.write('#\n')
        # listRegions = list(setRegions)
        
        # обработка описания движения поездов
        countTrain = 0 # кол-во обработанных поездов
        for i in fileTXT:
                        
            lineTXT = i.strip()
            if lineTXT == '':
                continue
            
            elif lineTXT[0] == '!':
                countTrain += 1
                fileTXTResult.write('\nПОЕЗД '+ str(countTrain) + '\n')            
                if stopCheck != 0:
                    break
                stopCheck = 0
                skipCheck = 0
                stations.clear()
                roleStations.clear()
                stations = [lineTXT[1:].split()]
                numberStation = 0
                for station in stations[0]:
                    if station in setStation:
                        roleStations.append(dictStation.get(station))
                    else:
                        numberErrors += 1
                        fileTXTResult.write('\n'+ lineTXT + '\t\t\tСПИСОК СТАНЦИЙ НЕ СФОРМИРОВАН\n')
                        fileTXTResult.write(station + ' СТАНЦИЯ ОТСУТСТВУЕТ В СПИСКЕ СТАНЦИЙ ДОРОГИ. Проверка сообщений этого поезда прервана. Ошибка '+ str(numberErrors)+'\n')
                        skipCheck +=1
                        break
                if len(stations[0]) == len(roleStations):
                    stations.append(roleStations)
                    fileTXTResult.write('\n'+lineTXT + '\t\t\tСПИСОК СТАНЦИЙ СФОРМИРОВАН\n')
                    stationsPassedThrough = []
                    listMessages.clear()
                    messageIPhrase.clear()
                    messageSPhrase.clear()
                    quantityTechnStation = checkQuantityRoleStation(roleStations, '1') + checkQuantityRoleStation(roleStations, '2')
                    quantityBoardStation = checkQuantityRoleStation(roleStations, '5')
                    continue

            if stopCheck > 0: # пропускаем обработку до конца файла
                continue

            elif (lineTXT[:2] == '(:'and lineTXT[-2:] != ':)'): # служебная фраза с информационной в след. строке
                if len(messageSPhrase) != 0:
                    skipCheck += 1
                    fileTXTResult.write('\n' + lineTXT + ' Служебная фраза не имеет информационной фразы. Проверка прервана.\n')
                    continue
                messageTemp = lineTXT[2:].split()
                resultCheckFormatSPhrase, messageSPhrase = checkFormatMessageSPhrase(messageTemp)
                fileTXTResult.write('\n' + lineTXT + '\t\t\t' + resultCheckFormatSPhrase + '\n')
                
                if len(messageSPhrase) < 13: # пополнение до полной фразы, если она не полная (полей меньше 13)
                    message = addingMessage(messageSPhrase.copy())
                else:
                    message = messageSPhrase.copy()
                
            elif lineTXT[:2] == '(:'and lineTXT[-2:] == ':)': # сообщение из служебной фразы
                messageTemp = lineTXT[2:-2].split()
                resultCheckFormatSPhrase, messageSPhrase = checkFormatMessageSPhrase(messageTemp)    
                
                
                fileTXTResult.write(lineTXT + '\t\t\t' + resultCheckFormatSPhrase + '\n\n')
                message = addingMessage(messageSPhrase.copy()) + messageIPhraseEmpty.copy()
                messageSPhrase.clear()
                listMessages.append(message.copy())
                message.clear()
                
                numberStation = checkLogicalMessage(numberStation, resultCheckFormatSPhrase)
                
                if stopCheck > 0:
                    break
            
            elif lineTXT[:2] != '(:'and lineTXT[-2:] == ':)': # информационная фраза со служеюной в предыд. строке
                messageTemp = lineTXT[:-2].split()
                if len(messageSPhrase) == 0:
                    fileTXTResult.write(lineTXT + '\t\tДля информационной фразы отсутствует служебная фраза. Проверка прервана.\n')
                    skipCheck += 1
                    continue
                resultCheckFormatIPhrase, messageTemp = checkFormatMessageIPhrase(messageTemp)    
                if resultCheckFormatIPhrase == 'МАКЕТ ВЕРЕН':
                    messageIPhrase = messageTemp.copy()
                else:
                    messageIPhrase = messageTemp.copy()
                fileTXTResult.write(lineTXT + '\t\t\t' + resultCheckFormatIPhrase + '\n\n')
                message = message + messageIPhrase
                listMessages.append(message.copy())
                messageSPhrase.clear()
                messageIPhrase.clear()
                message.clear()

                if resultCheckFormatSPhrase == 'МАКЕТ ВЕРЕН' and resultCheckFormatIPhrase == 'МАКЕТ ВЕРЕН':
                    resultCheckFormat = 'МАКЕТ ВЕРЕН'
                else:
                    resultCheckFormat = 'ОШИБКА МАКЕТА СООБЩЕНИЯ'
                
                numberStation = checkLogicalMessage(numberStation, resultCheckFormat)

            elif skipCheck == 1:
                fileTXTResult.write(lineTXT + '\t\tПроверка сообщения пропущена\n')
                
            else:
                fileTXTResult.write('\n' + lineTXT + '\t\t\tстрока не является частью сообщения\n')
        
        if countTrain < 5:
            numberErrors += 1
            fileTXTResult.write('Описано продвижение не всех поездов. Должно быть 5, описано ' + str(countTrain) + ' ОШИБКА ' + str(numberErrors)+ '.\n')
        fileTXT.close()
        fileTXTResult.close()
        if numberErrors != 0:
            nameFileTXTResultErr = nameFileTXTResult[:-4]+'_Err_'+str(numberErrors)+'.txt'
            if os.path.exists(nameFileTXTResultErr):
                os.remove(nameFileTXTResultErr)
            os.rename(nameFileTXTResult,nameFileTXTResultErr)
        print('*', end='')
        pass

print('\n\nОбработка завершена\n')
pass