# decodelab_task4
basic OCR text recognition using pytesseract, decode lab ai internship task


# Project 4 - Image/Text Recognition (Basic)

part of my decode lab ai internship tasks

## what it is

does basic text recognition (OCR) using pytesseract, which is just a python wrapper for tesseract, an already pretrained OCR engine. so we're not training any model ourselves here, just using an existing one, which is what the task wanted ("use a pre-trained model or simple library")

## how it works

didnt have a scanned document or image lying around to test on, so the script generates its own sample image with some text on it (using PIL/pillow) and then runs OCR on that same image to read the text back out

also prints:
- the recognized text
- a rough accuracy check (how many words matched the original text i put in the image)
- confidence score for each word it detected

## how to run

install these first:
```
pip install pillow pytesseract
```

AND you need tesseract itself installed on your system (not just the python package or it wont work):
- windows: https://github.com/UB-Mannheim/tesseract/wiki
- mac: `brew install tesseract`
- linux: `sudo apt install tesseract-ocr`

then run:
```
python proj4_text_recognition.py
```

## funny thing that happened

when i tested it, it actually misread "AI" as "Al" lol. guess capital I and lowercase l look basically the same to a computer too, made me laugh when i saw the output

## notes

accuracy depends a lot on image quality and font used. would be a better test to try this on an actual scanned or handwritten image sometime instead of a generated one, that would probably be way messier and harder to read for it
