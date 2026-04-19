from repository.matches.delete_match import delete_matchRepository
from flask import jsonify

def delete_match(match_id):
    result = delete_matchRepository(match_id)
    status_code = result.get('status_code', 500)
    return result, status_code