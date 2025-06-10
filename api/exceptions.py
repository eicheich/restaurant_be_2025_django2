from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django.core.exceptions import ValidationError


class ResourceNotFoundException(Exception):
    """Exception raised when a requested resource is not found."""
    pass


class InvalidRequestException(Exception):
    """Exception raised for invalid request data."""
    pass


def custom_exception_handler(exc, context):
    """
    Custom exception handler for REST framework views.
    """
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)

    # If the response is already handled by REST framework, return it
    if response is not None:
        return response

    # Otherwise, handle specific exceptions
    if isinstance(exc, ResourceNotFoundException):
        return Response(
            {'detail': str(exc) or 'Resource not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    elif isinstance(exc, InvalidRequestException):
        return Response(
            {'detail': str(exc) or 'Invalid request data'},
            status=status.HTTP_400_BAD_REQUEST
        )

    elif isinstance(exc, IntegrityError):
        return Response(
            {'detail': 'Database integrity error occurred'},
            status=status.HTTP_400_BAD_REQUEST
        )

    elif isinstance(exc, ValidationError):
        return Response(
            {'detail': str(exc)},
            status=status.HTTP_400_BAD_REQUEST
        )

    # For any unhandled exceptions, return a 500 error
    return Response(
        {'detail': 'An unexpected error occurred'},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
