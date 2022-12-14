"""modules"""
import json
import os
import ast
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#4from dotenv import load_dotenv
#from machinetranslation import url
#from machinetranslation import apikey

#load_dotenv()

apikey = 'Tvrv-7MnVoQtnB1-6cW4aFz4iExfX135kLFVqehODkkM'

url = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/f243fe1b-500a-4c5f-b0a2-2a753bc0d5b2'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_disable_ssl_verification(True)

language_translator.set_service_url(url)

def english_to_french(english):
    """translates english text string to french"""
    translation = language_translator.translate(
        text=english,
        model_id='en-fr').get_result()
    french_json = (json.dumps(translation, indent=2, ensure_ascii=False))
    french_dict = ast.literal_eval(french_json)
    french_text = ((french_dict['translations'])[0])['translation']
    return french_text

def french_to_english(french):
    """translates french text string to english"""
    translation = language_translator.translate(
        text=french,
        model_id='fr-en').get_result()
    english_json = (json.dumps(translation, indent=2, ensure_ascii=False))
    english_dict = ast.literal_eval(english_json)
    english_text = ((english_dict['translations'])[0])['translation']
    return english_text

