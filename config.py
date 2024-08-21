from dotenv import load_dotenv
from os import environ, path

current_directory = path.abspath(path.dirname(__file__))
env_path = path.join(current_directory, ".env")
load_dotenv(env_path)

default_max_file_size = 4 * 1000 * 1000 * 1000 # 4Go

class Config:
    SECRET_KEY = environ.get("SECRET_KEY")
    UPLOAD_DIRECTORY = environ.get("UPLOAD_DIRECTORY", "/tmp/")
    MAX_FILE_SIZE_BYTES = environ.get("MAX_FILE_SIZE", default_max_file_size)

