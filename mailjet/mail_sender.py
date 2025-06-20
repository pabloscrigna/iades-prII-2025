from mailjet_rest import Client

from secrets_key import API_KEY, SECRET_KEY


api_key = API_KEY
api_secret = SECRET_KEY

mailjet = Client(auth=(api_key, api_secret))

data = {
    "FromEmail": "pscrigna@gmail.com",
    "FromName": "Pablo Scrigna",
    "Subject": "Your email flight plan!",
    "Text-part": "Dear passenger, welcome to Mailjet! May the delivery force be with you!",
    "Html-part": '<h3>Dear passenger, welcome toMay the delivery force be with you!</h3>',
    "Recipients": [{"Email": "raulcabeza520@gmail.com"}],
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())
