import sys 


class HateSpeechException(Exception):
    def __init__(self,error_message,error_details):
        super().__init__(error_message)
        self.error_message=HateSpeechException.detailed_error_message(error_message=error_message,
                                                                      error_details=error_details)
        
    @staticmethod
    def detailed_error_message(error_message:Exception,error_details:sys):
        _, _,exc_trace=error_details.exc_info()
        file_name=exc_trace.tb_frame.f_code.co_filename
        line_number=exc_trace.tb_lineno
        
        error_message=f""" 
                        Error occurred in file {file_name},
                        line number {line_number},
                        error message is {str(error_message)}
                       """
        
        return error_message
    
    def __str__(self) -> str:
        return self.error_message