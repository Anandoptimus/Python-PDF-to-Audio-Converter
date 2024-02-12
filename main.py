from gtts import gTTS
import PyPDF2

pdf_file = open("notes pdf.pdf", "rb")
# load the pdf file

pdf_reader = PyPDF2.PdfReader(pdf_file)
# read the pdf file

count = len(pdf_reader.pages)
# count how many lines are there in the pdf

textList = []

for i in range(count):
        page = pdf_reader.pages[i]
        print(page)
        textList.append(page.extract_text())
print(textList)

# each line store it in a list without any new line

textString = " ".join(textList)
print(textString)
# changing the list to string

language = "en"
myAudio = gTTS(text=textString, lang=language, slow=False)
# converting the text into audio using google text to speech (gTTS)
myAudio.save("Audio.mp3")
