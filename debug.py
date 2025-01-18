import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Fetch the DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Print the DATABASE_URL
if DATABASE_URL:
    print(f"DATABASE_URL: {DATABASE_URL}")
else:
    print("DATABASE_URL is not set or could not be loaded.")
