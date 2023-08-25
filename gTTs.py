from gtts import gTTS
import os
import time
import random
name=(input('what is your name: '))
print('hi',name,'today we are going to lern abote gtts and its ability to tern text to spech for exampel')
time.sleep(1)
def text_to_spech(mytext):
    audio=gTTS(text=mytext,slow=False)
    audio_file= 'audio.mp3'
    audio.save(audio_file)
    os.system(audio_file)
text_to_spech('this is the exampel')

print('if you want to use text to spech you have to: ')
print('_____________________________________________')
time.sleep(3)

print('1,install and import gTTS importing it will be like this from gtts import gTTS ')
print('_____________________________________________')
time.sleep(3)

print('2,you can use os to reed your file')
print('_____________________________________________')
time.sleep(3)

print('3,then you have to use the mathod gTTS with this you can change the languge and the speed')
print('you dont have to give it the languge or the speed veribel but you have to give it the text')
print('_____________________________________________')
time.sleep(3)

print('4,then you seve the file like so audio.save(audio_file)')
print('_____________________________________________')
time.sleep(3)

print('5,now the only thing that is left is to reed it a esay way i fond was to use os.system(saved_file_name)')
print('_____________________________________________')
time.sleep(3)

print('6,other things to note are :')
print('_____________________________________________')
time.sleep(3)

print('7,the value of speed is a bool witch means it can be true or false')
print('_____________________________________________')
time.sleep(3)

print('8,you have to difine the fils format like mp3')
print('_____________________________________________')
time.sleep(3)

print('10,and be carful not to seve the original file that you did not put in the gtts Engine ')
print('_____________________________________________')
time.sleep(3)
print('12,last one your text has to be str')
print('_____________________________________________')
text_to_spech('do you want to test it out')
answer=(input(': '))
while True:
    if answer == "yes":
        text3=(input('then give me a text: '))
        text_to_spech(text3)
        answer=(input('do you want to do it agine ? : '))
    elif answer == "no":
        print('by then :) :')
        break
    else :
        print('try yes and no')
        answer=(input(': '))