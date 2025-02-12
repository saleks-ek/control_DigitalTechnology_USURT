"""
Проверка контрольной работы по дисциплине "Цифровые технологии в профессональной деятельности"
"""
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

# checkStation(station)


import os

os.chdir('Для проверки//')
fileList = os.listdir() 
for nameFileTXT in fileList:
    fileTXT = open(nameFileTXT, 'r')
    fileTXTResult = open(nameFileTXT[0:len(nameFileTXT)-4]+'_result'+'.txt', 'w')
    for i in fileTXT:
        lineTXT = i.strip()
        # pass
        if lineTXT == '#':
            break
        else:
             res = checkNumber(lineTXT)
             fileTXTResult.write(lineTXT + ' '+ res+'\n')
    fileTXTResult.write('#\n')
    for i in fileTXT:
        lineTXT = i.strip()
        if lineTXT == '#':
            break
        else:
            res = checkStation(lineTXT)
            fileTXTResult.write(lineTXT + ' '+ res+'\n')
    fileTXTResult.write('#\n')
fileTXT.close()
fileTXTResult.close()
print('Обоработка завершена')
pass