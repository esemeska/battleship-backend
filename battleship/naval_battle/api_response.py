from enum import Enum
from rest_framework.response import Response
from rest_framework import status

class ApiResponse:
    @staticmethod
    def success(message, data=None, status_code=status.HTTP_200_OK):
        if data is not None:
            return Response({'message': message, 'data': data}, status=status_code)
        return Response({'message': message}, status=status_code)

    @staticmethod
    def error(message, status_code=status.HTTP_400_BAD_REQUEST):
        return Response({'error': message}, status=status_code)


    class Auth(Enum):
        NOT_VALID = "{} is not valid"
        SHORT = "{} is very short"
        SAFE = "{} is not safe"
        EXISTS = "{} already exists"
        
        def format(self, field):
            return self.value.format(field)
