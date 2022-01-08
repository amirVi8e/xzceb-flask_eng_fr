'''
    This Package is meant to translate French to English and English to French
'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2022-01-08'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    #write the code here
    '''
    This method is to translate text from English to French
    '''
    if english_text is not None:
        translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        french_text_var = json.loads(json.dumps(translation, indent=2, ensure_ascii=False))

        french_text = french_text_var['translations'][0]['translation']
        return french_text
    return None

def french_to_english(french_text):
    #write the code here
    '''
    This method is to translate text from French to English
    '''
    if french_text is not None:
        translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        english_text_var = json.loads(json.dumps(translation, indent=2, ensure_ascii=False))

        english_text = english_text_var['translations'][0]['translation']
        return english_text
    return None
