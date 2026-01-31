"""
response_formatter.py

Utility module for formatting API responses in AI-Powered Smart Interview System.
Provides consistent response structure across all API endpoints.
"""

from typing import Any, Dict, Optional


def format_success_response(
    data: Any,
    message: str = "Success"
) -> Dict[str, Any]:
    """
    Format a successful API response.
    
    Args:
        data: The response payload/data
        message: Optional success message
        
    Returns:
        dict: Formatted success response
    """
    return {
        "success": True,
        "message": message,
        "data": data,
    }


def format_error_response(
    error: str,
    status_code: int = 500,
    details: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Format an error API response.
    
    Args:
        error: Error message
        status_code: HTTP status code
        details: Optional error details
        
    Returns:
        dict: Formatted error response
    """
    response = {
        "success": False,
        "error": error,
        "status_code": status_code,
    }
    
    if details:
        response["details"] = details
        
    return response


def format_validation_error(
    field: str,
    message: str
) -> Dict[str, Any]:
    """
    Format a validation error response.
    
    Args:
        field: Field name that failed validation
        message: Validation error message
        
    Returns:
        dict: Formatted validation error
    """
    return {
        "success": False,
        "error": "Validation Error",
        "field": field,
        "message": message,
    }
