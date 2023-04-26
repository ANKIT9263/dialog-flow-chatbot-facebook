import falcon
import json

from dialogflow_chatbot.chafra.bot import BotRequest
from dialogflow_chatbot.channels.whatsapp import WhatsApp
from dialogflow_chatbot.get_response import WhatsAppDialogflow


class WhatsAppWebhookResource:
    def __init__(self):
        self.dialogflow = WhatsAppDialogflow()

    def on_post(self, req, resp):
        data = req.media

        if 'messages' in data:
            bot_id = data['messages'][0].get('to', None) if data.get('messages', None) else None
            user_id =  data.get('contacts')[0].get('wa_id')
            text = data['messages'][0].get('text', {}).get('body',None) if data.get('messages', None) else None

        whatsapp = WhatsApp()

        bot_request = BotRequest(text, "WHATSAPP", bot_id, user_id, annotate=True)


        # Set the response status code and body
        resp.status = falcon.HTTP_200

    @staticmethod
    def _process_message(bot, bot_request, whatsapp, data, user_id):
        bot_responses, dm_context, utt_id = bot.process(bot_request, return_dm_context=True, return_utt_id=True)
        for bot_response in bot_responses:
            whatsapp.reply(bot_response, dm_context, bot_request=bot_request, utt_id=utt_id)

        return