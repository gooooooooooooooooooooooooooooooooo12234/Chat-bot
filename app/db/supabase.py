

from supabase import create_client
from app.core.config import settings
import os



# for local machine testing using .env file ... dotenv lib and load_dotenv() function 
# os is better for deploying 

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")


class SupabaseClient:
    def __init__(self):
        self.client = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_KEY
        )
        
    def get_client(self):
        return self.client
    
    
sb = SupabaseClient()