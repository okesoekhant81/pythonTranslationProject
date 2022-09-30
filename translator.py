from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
import os

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(
        version = '2018-05-01',
        authenticator=authenticator
    )
lt.set_service_url(url)

def english_to_french(engtxt):
    french_translator = lt.translate(
        text=engtxt, model_id='en-fr'
    ).get_result()
    return french_translator.get('translations')[0].get('translation')

def french_to_english(ftxt):
    english_translator = lt.translate(
        text=ftxt, model_id='fr-en'
    ).get_result()
    return english_translator.get('translations')[0].get('translation')
