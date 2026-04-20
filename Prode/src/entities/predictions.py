from datetime import datetime

Prediction = {
    "id": int,
    "user_id": int,
    "fixture_id": int,
    "predicted_local_goals": int,
    "predicted_visitor_goals": int,
    "created_at": datetime,
}