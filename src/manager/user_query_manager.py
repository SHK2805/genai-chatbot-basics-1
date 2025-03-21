from src.services.user_query_service import UserQueryService

class UserQueryManager:
    def handle_query(self, user_query: str) -> str:
        query_service = UserQueryService()
        return query_service.process_query(user_query)
