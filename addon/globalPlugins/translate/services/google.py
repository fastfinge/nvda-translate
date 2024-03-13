from googletrans import Translator as GoogleTrans
from translator import Translator
from urllib.parse import urlparse

class GoogleTranslator(Translator):
	def __init__(self):
		self._api_key = None
		self._server_url = None
		self._supported_languages = None
		self._google_translator = GoogleTrans(raise_exception=True)
		self.supported_languages = self._google_translator.LANGUAGES

	def translate(self, text, from_lang, to_lang):
		# Overriding the translate method to use googletrans
		if from_lang not in self._supported_languages:
			raise ValueError(f"Unsupported source language: {from_lang}")
		if to_lang not in self._supported_languages:
			raise ValueError(f"Unsupported target language: {to_lang}")
		translation = self._google_translator.translate(text, src=from_lang, dest=to_lang)
		return translation.text

	@property 
	def api_key(self):
		return self._api_key

	@api_key.setter
	def api_key(self, value):
		self._api_key = value

	@property
	def server_url(self):
		return self._server_url

	@server_url.setter
	def server_url(self, value):
		parsed_url = urlparse(value)
		if all([parsed_url.scheme, parsed_url.netloc]):
			if value.contains("google"):
				self._server_url = value
				self._google_translator = GoogleTrans(raise_exception=True, service_urls=value)
			else:
				raise ValueError("Invalid URL: URL must contain google.")
		else:
			raise ValueError("Invalid URL")

	@property
	def supported_languages(self):
		return self._supported_languages

	@supported_languages.setter
	def supported_languages(self, value):
		if isinstance(value, dict):
			self._supported_languages = value
		else:
			raise ValueError("Supported languages must be a dictionary")
