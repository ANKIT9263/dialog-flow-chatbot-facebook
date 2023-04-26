from dialogflow_chatbot.chafra.webhooks.dialogflow import DialogFlow
from dialogflow_chatbot.channels.whatsapp import WhatsApp


class WhatsAppDialogflow:
    def __init__(self):
        pass
    
    def handle_message(self, message):
        # Get the sender's phone number and message text
        sender_number = message['From'].replace('whatsapp:', '')
        message_text = message['Body']

        # Send the message to Dialogflow and get the response

        response_text = DialogFlow(sender_number).send_message_to_dialogflow(message_text)

        # Send the response to WhatsApp
        WhatsApp.send_message_to_whatsapp(sender_number, response_text)
