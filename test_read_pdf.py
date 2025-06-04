""" Извлечение текста из файла ПДФ формата и сохранение его к формат TXT"""

from pypdf import PdfReader
import os

countFiles = 0
pathForCheckPDF = 'Для проверки/' # папка хранения проверяемых файлов
fileList = os.listdir(pathForCheckPDF)

for nameFilePDF in fileList:
    if nameFilePDF[-3:] != 'pdf': # открываем файлы только с расширением pdf
        continue
    else:
        text = ''
        reader = PdfReader(pathForCheckPDF+nameFilePDF)
        for page_number, page in enumerate(reader.pages, start=1):
            text = text + page.extract_text() + '\n'
        
        textLine = text.split(sep="\n")
        fileTXTResult = open(pathForCheckPDF+nameFilePDF[0:len(nameFilePDF)-3]+ 'txt', 'w', encoding = 'utf-8')
        for line in textLine:
            if line[:1] == '!':
                fileTXTResult.write('\n' + str(line) + '\n')     
            else:
                fileTXTResult.write(str(line) + '\n') 
        fileTXTResult.close()
        countFiles += 1
       
print('Обраобтано файлов ' + str(countFiles))
pass