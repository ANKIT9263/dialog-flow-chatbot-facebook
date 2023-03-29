from google.cloud import dialogflow_v2beta1 as dialogflow
from google.api_core.exceptions import InvalidArgument
from google.protobuf.json_format import MessageToDict

class DialogFlow:
    def __init__(self, session_id):
        DIALOGFLOW_PROJECT_ID = 'catalogflow-ujsa'
        SESSION_ID = session_id
        self.DIALOGFLOW_LANGUAGE_CODE = 'en'
        GOOGLE_APPLICATION_CREDENTIALS = '/Users/ankit/.config/gcloud/application_default_credentials.json'
        self.session_client = dialogflow.SessionsClient()
        self.session = self.session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)


    def get_response(self, text_to_be_analyzed):
        text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=self.DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        try:
            response = self.session_client.detect_intent(session=self.session, query_input=query_input)
        except InvalidArgument:
            raise
        response = MessageToDict(response._pb)
        custom_response = response['queryResult']['fulfillmentMessages'][1]['payload']
        return custom_response