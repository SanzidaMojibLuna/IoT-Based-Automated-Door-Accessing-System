from twilio.rest import Client

def send_message():
	account_sid = [tw7923648]
	auth_token = [abdtmol973wls]
	client = Client(account_sid, auth_token)
	message = client.messages.create(body='Mr. X is in distress and need immediate assistance!', from_=[012836321], to=[0817362791])
	print(message.sid)