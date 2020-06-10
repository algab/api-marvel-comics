import os
import hashlib
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def generate_keys():
    timestamp = str(datetime.timestamp(datetime.now()))
    public_key = os.getenv('PUBLIC_KEY')
    private_key = os.getenv('PRIVATE_KEY')
    hash = hashlib.md5('{}{}{}'.format(timestamp, private_key, public_key).encode()).hexdigest() 
    return timestamp, public_key, hash