from datetime import datetime

Fixture = {
    "id": int,
    "local_team": str,
    "visitor_team": str,
    "stadium": str,
    "city": str,
    "date_time": datetime, 
    "local_goals": int,
    "phase": str,
    "visitor_goals": int,
}
