from contracts.response.ranking_response import ranking_list_response
from infrastructure.errors.ranking import ErrRankingPaginacionInvalida
from repository.ranking.get_ranking import count_users, fetch_ranking_page


def execute(limit: int, offset: int, base_url: str, max_limit: int) -> dict:
    if limit < 1 or offset < 0 or limit > max_limit:
        return ErrRankingPaginacionInvalida

    total = count_users()
    rows = fetch_ranking_page(limit, offset)
    return ranking_list_response(rows, total, limit, offset, base_url)
