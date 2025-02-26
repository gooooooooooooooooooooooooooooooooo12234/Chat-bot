

import re
from typing import Dict, Any, List
from langgraph.graph import StateGraph, END
from app.db.supabase import sb
from agent.function_map import extract_intent, extract_team_members, register_for_event


