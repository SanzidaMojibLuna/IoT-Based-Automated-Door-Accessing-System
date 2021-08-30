from gtts import gTTS
import os


def voice_alert_ID(who):
	language = 'en'
	if who == 'unknown':
		alert = 'unknown person is at the door'
	else
		alert = who +' is at the door'

	myobj = gTTS(text=who, lang=language, slow=False)
	myobj.save("alert.mp3")
	os.system("alert.mp3")


def voice_alert_ask():
	language = 'en'
	ask = 'do you want to open the door?'
	myobj = gTTS(text=ask, lang=language, slow=False)
	myobj.save("ask.mp3")
	os.system("ask.mp3")

voice_alert_enter():
	language = 'en'
	ask = 'door is open'
	myobj = gTTS(text=ask, lang=language, slow=False)
	myobj.save("enter.mp3")
	os.system("enter.mp3")	

voice_alert_close():
	language = 'en'
	ask = 'door is closed'
	myobj = gTTS(text=ask, lang=language, slow=False)
	myobj.save("close.mp3")
	os.system("close.mp3")

voice_alert_deny():
	language = 'en'
	ask = 'door will not be opened'
	myobj = gTTS(text=ask, lang=language, slow=False)
	myobj.save("deny.mp3")
	os.system("deny.mp3")	

say_again():
	language = 'en'
	ask = 'command is no clear. please try again'
	myobj = gTTS(text=ask, lang=language, slow=False)
	myobj.save("say_again.mp3")
	os.system("say_again.mp3")

metal_alert(metal):
	language = 'en'
	ask = ''
	if metal == 1 :
		ask = 'this person is carrying metal'
	else : 
		ask = 'this person is not carrying metal'

	myobj = gTTS(text=ask, lang=language, slow=False)
	myobj.save("metal.mp3")
	os.system("metal.mp3")	