import os 
from dotenv import load_dotenv
load_dotenv()
print("KEY:", os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"))