import os
from dotenv import load_dotenv
load_dotenv(os.getenv('ENV_FILE', '.env'))
print(os.environ['MONGO_USER'])