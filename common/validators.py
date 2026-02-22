from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.utils.deconstruct import deconstructible


@deconstructible
class OnlyLetterValidator:
    def __init__(self, message: str="The name must include only letters!") -> None:
        self.__message = message

    def __call__(self, value: str):
        for char in value:
            if not char.isalpha():
                raise ValidationError(self.__message)



@deconstructible
class FileSizeValidator:
    def __init__(self, file_size: int, message:str=None) -> None:
        self.file_size = file_size # MB - megabytes
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value: str):
        if not value:
            self.__message = f"Photo size must not exceed {self.file_size}MB!"

        self.__message = value

    def __call__(self, file: UploadedFile):
        if file.size > self.file_size * 1024 * 1024:  # MB * 1024 -> KB * 1024 -> Bytes
            raise ValidationError(self.message)