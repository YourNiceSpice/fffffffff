import dotenv
import os
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
host = os.environ["HOST"]
current_chat = os.environ['C_CHAT']
token = os.environ['TOKEN']
os.environ["TOKEN"] = 'res'
dotenv.set_key(dotenv_file, "TOKEN", os.environ["TOKEN"])
token = os.environ['TOKEN']

q=1