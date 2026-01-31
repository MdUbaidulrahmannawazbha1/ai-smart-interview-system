"""
Response formatting utilities
"""
from typing import Any, Dict, Optional


def success_response(data: Any, message: str = "Success") -> Dict[str, Any]:
    """
    Format success response
    
    Args:
        data: Response data
        message: Success message
        
    Returns:
        Formatted response dictionary
    """
    return {
        "status": "success",
        "message": message,
        "data": data
    }


def error_response(message: str, error_code: Optional[str] = None) -> Dict[str, Any]:
    """
    Format error response
    
    Args:
        message: Error message
        error_code: Optional error code
        
    Returns:
        Formatted error response dictionary
    """
    response = {
        "status": "error",
        "message": message
    }
    
    if error_code:
        response["error_code"] = error_code
    
    return response


def paginated_response(
    data: list,
    total: int,
    page: int = 1,
    page_size: int = 10
) -> Dict[str, Any]:
    """
    Format paginated response
    
    Args:
        data: List of items for current page
        total: Total number of items
        page: Current page number
        page_size: Items per page
        
    Returns:
        Formatted paginated response
    """
    total_pages = (total + page_size - 1) // page_size
    
    return {
        "status": "success",
        "data": data,
        "pagination": {
            "page": page,
            "page_size": page_size,
            "total_items": total,
            "total_pages": total_pages,
            "has_next": page < total_pages,
            "has_prev": page > 1
        }
    }
