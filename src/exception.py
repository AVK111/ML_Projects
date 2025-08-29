# ...existing code...
import sys
from typing import Any
from src.logger import logging

def error_message_detail(error: Exception, error_detail: Any = sys) -> str:
   
    exc_info = error_detail.exc_info()
    if not exc_info or exc_info[2] is None:
        return f"Error message [{str(error)}]"

    _, _, exc_tb = exc_info
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message = (
        "Error occurred in python script name [{0}] line number [{1}] error message [{2}]"
        .format(file_name, line_no, str(error))
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: Any = sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message

