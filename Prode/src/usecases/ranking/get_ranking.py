from contracts.response.ranking_response import ranking_list_response
from infrastructure.errors.ranking import ErrRankingPaginacionInvalida
from repository.ranking.get_ranking import count_users, fetch_ranking_page, DEFAULT_LIMIT, MAX_LIMIT


def execute(limit: int = DEFAULT_LIMIT, offset: int = 0) -> dict:
    if limit < 1 or offset < 0 or limit > MAX_LIMIT:
        return ErrRankingPaginacionInvalida
    
    total = count_users()
    rows = fetch_ranking_page(limit, offset)
    return ranking_list_response(rows, total, limit, offset, "")
