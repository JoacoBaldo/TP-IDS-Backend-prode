from repository.matches.delete_match import delete_match

def delete_match_endpoint(match_id):
    return delete_match(match_id)