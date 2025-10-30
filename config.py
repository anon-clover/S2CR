import os
import logging


OPENAI_API_BASE_URL = ""
OPENAI_API_KEY = ""
OPENAI_API_MODEL = ""


ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
SRC_PATH = os.path.join(ROOT_PATH, "src")
DATA_PATH = os.path.join(ROOT_PATH, "data")
EXTERNAL_DATA_PATH = os.path.join(DATA_PATH, "external")
PROCESSED_DATA_PATH = os.path.join(DATA_PATH, "processed")
RAW_DATA_PATH = os.path.join(DATA_PATH, "raw")

"""NLTK"""
NLTK_DATA_PATH = os.path.join(EXTERNAL_DATA_PATH,"nltk_data")

"""log"""
logger = logging.getLogger("logger")