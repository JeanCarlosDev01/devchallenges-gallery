from dotenv import load_dotenv
import os

load_dotenv()

def check_password(password: str):
    if password == os.getenv('REGISTER_PASSWORD'):
        return True
    return False