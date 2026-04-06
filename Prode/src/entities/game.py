from datetime import datetime

Fixture = {
    "id": int,
    "local_team": str,
    "visitor_team": str,
    "stadium": str,
    "city": str,
    "date_time": datetime.datetime, 
    "local_goals": int,
    "phase": str,
    "visitor_goals": int,
}


Prediction = {
    "user_id": int,
    "game_id": int,
    "predicted_local_goals": int,
    "predicted_visitor_goals": int,
}
