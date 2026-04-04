from datetime import datetime

Fixture = {
    "id": int,
    "local_team": str,
    "visitor_team": str,
    "stadium": str,
    "city": str,
    "date_time": datetime.datetime, 
    "phase": str,
}

Result = {
    "game_id": int,
    "local_goals": int,
    "visitor_goals": int,
    "create_at": datetime.datetime,
}

Prediction = {
    "user_id": int,
    "game_id": int,
    "predicted_local_goals": int,
    "predicted_visitor_goals": int,
}
