from enum import Enum

 # genius 
class ResponseSignals(Enum):
   FILE_TYPE_NOT_SUPPORTED = "invalid file type "
   FILE_SIZE_EXCEEDS_LIMIT = "file size exceeds the maximun allowed size"
   FILE_VALIDATED_SUCCESS= "file is valid"
   FILE_UPLOADED_FAILED ="file upload failed"
   FILE_UPLOADED_SUCCESS = "file uploaded successfully"