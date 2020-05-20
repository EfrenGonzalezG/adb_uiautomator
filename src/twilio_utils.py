from credentials import twilio_cred
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say


def make_call(message, _to, _from):
    account_sid = twilio_cred['account_sid']
    auth_token = twilio_cred['auth_token']
    response = VoiceResponse()
    response.pause(length=10)
    response.say(message, voice='woman', language='es')
    client = Client(account_sid, auth_token)
    call = client.calls.create(
                            twiml=response,
                            to=_to,
                            from_=_from,
                            timeout=120,
                        )
