from cerberus import Validator
import re
from rest_framework.response import Response
from config.messages import Messages
from cerberus import errors, Validator

from rest_framework import status

class CustomValidator(Validator):
    
    def _validate_isEmail(self, isEmail, field, value):
        print('type',type(isEmail))
        """ Test the valid email.
        The rule's arguments are validated against this schema:
        {'type': 'string'}
        """
        try:
            if isEmail: 
                x = re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value)
            if (x):
                return True
            else: 
                self._error(field,"has invalid format")
        except BaseException as e:
            return Response({'error': Messages.SOMETHING_WENT_WRONG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def _validate_isAllowed(self,isAllowed, field, value):
        try:
            if isAllowed: 
                if value == 0:
                    self._error(field,"cannot be 0") 
                else: 
                    return True
        except BaseException as e:
            return Response({'error': Messages.SOMETHING_WENT_WRONG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ValidateExcelData:
    
    def isValidEmail(email):
 
        if re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email) != None:
            return True
        else:
            return False

    def isValidPhone(phone):
        
        if re.match("^[0-9]{10}$", phone) != None:
            return True
        else:
            return False

