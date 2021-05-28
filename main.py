import cv2
import numpy as np
import RPi.GPIO as GPIO
import os

cap = cv2.VideoCapture(0)
flag = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

import os.path 

lang_full = ("english", "Gujarati", "Hindi", "Kannada", "Malayalam", "tamil", "urdu")
lang_code = {"en", "gu", "hi", "kn", "ml", "ta", "ur"}

lang_file = open("lang.txt", "wb")
if os.path.isfile("lang.txt"):
    print("file exist no ne")
else:
    fo = open("foo.txt", "wb")
    fo.write("0")
    print("created file and wrote 0")

os.system("play audio/hello.mp3")
str = fo.read(1);
lang_num = int(str)
print("Selected lang : ")
print(lang_full[int(str)]) 

curr_lang = lang_code[lang_num]
while(1):
    if GPIO.input(11) == GPIO.HIGH:
        print("next lang")
        if (lang_num>6):
            lang_num = 0;

        print(lang_code[lang_num])
        curr_lang = lang_code[lang_num]
        fo = open("foo.txt", "wb")
        fo.write(lang_num)

    ret, frame = cap.read()
    gray_vid = cv2.cvtColor(frame, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Original',frame)
    edged_frame = cv2.Canny(frame,100,200)
    cv2.imshow('Edges',edged_frame)
    k= cv2.waitKey(5) & 0xFF
    if GPIO.input(10) == GPIO.HIGH:
        print('You Pressed A Key!')
        cv2.imwrite('images/c1.png',frame)
        flag = True
        break  # finishing the loop
    
# Quit with 'Esc' key
    
    #if k==27:
     #   break
cap.release()
cv2.destroyAllWindows()


from botocore.exceptions import NoCredentialsError
import key as config

ACCESS_KEY = config.accesKey
SECRET_KEY = config.accesSecret

import boto3

# Document
s3BucketName = "mytextextract"
documentName = "images/c1.png"
s3_file = 'c1.png'
#upload file 
def upload_to_aws(documentName, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(documentName, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploadFlag = False
if(flag):
    uploaded = upload_to_aws(documentName, 'mytextextract', s3_file)
    uploadFlag = True

# Amazon Textract client

textract = boto3.client('textract', region_name='us-east-1',aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

# Call Amazon Textract
response = textract.detect_document_text(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': s3_file
        }
    })

#print(response)
content = ""
malayalam = ""
updatedMalayalam = ""
# Print detected text
contentFlag = False
if(uploadFlag):
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            content +=  item["Text"]
if(len(content)>2):
    print(content.encode('utf-8'))
    contentFlag = True;


from gtts import gTTS
def play(text):
    tts = gTTS(text, lang='ta')
    tts.save('hello.mp3')
    print("saved")

def translate(Englishtext):
    translate = boto3.client('translate',region_name='us-east-1',aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    result = translate.translate_text(Text=Englishtext,
                                  SourceLanguageCode="en",
                                  TargetLanguageCode="ta")
    malayalam= result["TranslatedText"]
    print(malayalam.encode('utf-8'))
    print(len(malayalam))
    play(malayalam)
    #print(updatedMalayalam)
    #print(f'TranslatedText: {result["TranslatedText"]}')
    #print(f'SourceLanguageCode: {result["SourceLanguageCode"]}')
    #print(f'TargetLanguageCode: {result["TargetLanguageCode"]}')
if(contentFlag):
    translate(content)
    print(updatedMalayalam)
    
def playMusic(file):
    from soundplayer import SoundPlayer
    p = SoundPlayer(file, 1)        
    print("playing"+file)
    p.play() # non-blocking, volume = 0.5
    print ("done")

if(contentFlag):
    os.system("play hello.mp3")
    #playMusic("hello.mp3")
    flag = False
    uploadFlag = False
    contentFlag = False