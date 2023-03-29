

from dialogflow_chatbot.whatsapp import WhatsApp
from dialogflow_chatbot.dialogflow import DialogFlow

user_text = "catalog"
user_id = '96550761600'

dialogflow = DialogFlow(session_id=user_id)
dialogflow_response = dialogflow.get_response(user_text)

whatsapp = WhatsApp()
whatsapp.send_text(dialogflow_response)


