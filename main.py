''' This is simple project which will help to read each and every line of the pdf no matter the number of pages in pdf'''

#Here we are importing pyttsx3 and PyPDF2 library
import pyttsx3
import PyPDF2

#here, we are creating a new variable name 'book' in which we are openning the pdf  and reading the pdf into binary.
book = open('oop.pdf', 'rb')

#here, we are reading the entire book by using PyPDF2.PdfFileReader
pdfReader = PyPDF2.PdfFileReader(book)

#here, we are counting the number of pages in pdf and storing it into a pages
pages = pdfReader.numPages

#And then here w are excessing the pdf and letting the speaker to speak each and every line of the pdf
speaker = pyttsx3.init()

#here, we are using for loop to read from starting of the pages 0 and to the end of the pages
for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
