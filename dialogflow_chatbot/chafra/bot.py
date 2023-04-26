

class BotRequest:   # used for accessing bot request
    def __init__(self, text, channel, bot_id, user_id, annotate, user_name = None,
                 image_url = None,location=None, wa_location=None, voice_url=None,video_url=None,
                 document_url=None, sticker_url=None, story_mention=None,
                 story_reply=None,ig_message_id=None, wa_channel_360=None, button_id=None,
                 wa_contact=None, catalog_order=None, catalog_referred_product=None,
                 message_event=None,message_id=None, reply_to=None, custom_timestamp=None):

        self._channel = channel
        self._wa_channel_360 = wa_channel_360
        self._bot_id = bot_id
        self._user_id = user_id
        self._text = text
        self._location = location
        self._wa_location = wa_location
        self._custom = None
        self._file = None
        self._image = None
        self._image_url = image_url
        self._voice_url = voice_url
        self._document_url = document_url
        self._sticker_url = sticker_url
        self._video_url = video_url
        self._story_mention_url = story_mention
        self._story_reply_url = story_reply
        self._ig_mid = ig_message_id
        self._annotate = annotate
        self._user_name = user_name
        self._button_id = button_id
        self._wa_contact = wa_contact
        self._catalog_order = catalog_order
        self._catalog_referred_product = catalog_referred_product
        self._message_event = message_event
        self._flowbot_reply = None
        self._message_id = message_id
        self._reply_to = reply_to
        self._utt_id = None
        self._custom_timestamp = custom_timestamp


    def get_channel(self):
        return self._channel

    def get_wa_channel_360(self):
        return self._wa_channel_360

    def get_bot_id(self):
        return self._bot_id

    def get_user_id(self):
        return self._user_id

    def get_user_name(self):
        return self._user_name

    def get_text(self):
        return self._text

    def get_message_id(self):
        return self._message_id

    def get_reply_to(self):
        return self._reply_to

    def set_annotate(self, annotate):
        self._annotate = annotate

    def get_annotate(self):
        # whether to annotate the bot response or not - boolean value
        return self._annotate

    def set_text(self, text):
        self._text = text

    def set_location(self, longitude, latitude, address):
        self._location = {
            'longitude': longitude,
            'latitude': latitude,
            'address': address
        }

    def get_location(self):
        return self._location

    def set_wa_location(self, longitude, latitude):
        self._wa_location = {
            'longitude': longitude,
            'latitude': latitude
        }

    def get_wa_location(self):
        return self._wa_location

    def set_wa_contact(self, contact_object):
        self._wa_contact = contact_object

    def get_wa_contact(self):
        return self._wa_contact

    def set_catalog_order(self, catalog_order):
        self._catalog_order = catalog_order

    def get_catalog_order(self):
        return self._catalog_order

    def set_catalog_referred_product(self, catalog_referred_product):
        self._catalog_referred_product = catalog_referred_product

    def get_catalog_referred_product(self):
        return self._catalog_referred_product

    def set_message_event(self, message_event):
        self._message_event = message_event

    def get_message_event(self):
        return self._message_event

    def set_image(self, type, url):
        self._image = {
            'type': type,
            'url': url
        }

    def get_image(self):
        return self._image

    def set_utt_id(self, utt_id ):
        self._utt_id = utt_id

    def get_utt_id(self):
        return self._utt_id

    def set_custom_timestamp(self, custom_timestamp ):
        self._custom_timestamp = custom_timestamp

    def get_custom_timestamp(self):
        return self._custom_timestamp

    def set_image_url(self, url):
        self._image_url = url

    def get_image_url(self):
        return self._image_url

    def set_document_url(self, url):
        self._document_url = url

    def get_document_url(self):
        return self._document_url

    def set_video_url(self, url):
        self._video_url = url

    def get_video_url(self):
        return self._video_url

    def set_sticker_url(self, url):
        self._sticker_url = url

    def get_sticker_url(self):
        return self._sticker_url


    def get_whatsapp_flowbot_reply(self):
        return self._flowbot_reply

    def set_voice_url(self, url):
        self._voice_url = url

    def get_voice_url(self):
        return self._voice_url

    def set_story_mention_url(self, story_mention_url):
        self._story_mention_url = story_mention_url

    def get_story_mention_url(self):
        return self._story_mention_url

    def set_story_reply_url(self, story_reply_url):
        self._story_reply_url = story_reply_url

    def get_story_reply_url(self):
        return self._story_reply_url

    def set_ig_mid(self, ig_mid):
        self._ig_mid = ig_mid

    def get_ig_mid(self):
        return self._ig_mid

    def set_file(self, type, url):
        self._file = {
            'type': type,
            'url': url
        }

    def get_file(self):
        return self._file

    def get_custom(self):
        return self._custom

    def set_custom(self, custom):
        self._custom = custom

    def get_button_id(self):
        return self._button_id

    def set_button_id(self, button_id):
        self._button_id = button_id

    def to_dict(self):
        d = dict()
        if self.get_text():
            d['text'] = self.get_text()

        if self.get_channel():
            d['channel'] = self.get_channel()

        if self.get_user_id():
            d['user_id'] = self.get_user_id()

        # if self.get_user_name():
        #     d['user_id'] = self.get_user_name()

        if self.get_bot_id():
            d['bot_id'] = self.get_bot_id()

        if self.get_location():
            d['location'] = self.get_location()

        if self.get_image():
            d['location'] = self.get_image()

        if self.get_custom():
            d['custom'] = self.get_custom()

        if self.get_file():
            d['file'] = self.get_file()

        if self.get_image():
            d['image'] = self.get_image()

        if self.get_message_id():
            d['message_id'] = self.get_message_id()

        if self.get_reply_to():
            d['reply_to'] = self.get_reply_to()

        if self.get_wa_contact():
            contact = self.get_wa_contact()
            d['wa_contact'] = contact

        if self.get_story_mention_url():
            d['type'] = 'story_mention'
            d['story_id'] = self.get_message_id()
            d['story_url'] = self.get_story_mention_url()

        if self.get_story_reply_url():
            d['type'] = 'story_reply'
            d['story_id'] = self.get_message_id()
            d['story_url'] = self.get_story_reply_url()
            d['message'] = self.get_text()

        if self.get_catalog_order():
            d['catalog_order'] = self.get_catalog_order()

        if self.get_catalog_referred_product():
            d['catalog_referred_product_id'] = self.get_catalog_referred_product()

        return d
