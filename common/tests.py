from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from common.validators import OnlyLetterValidator, FileSizeValidator


class OnlyLetterValidatorTests(TestCase):
    def setUp(self):
        self.validator = OnlyLetterValidator()

    def test_valid_name_passes(self):
        try:
            self.validator('John Doe')
        except ValidationError:
            self.fail('OnlyLetterValidator raised ValidationError on a valid name')

    def test_name_with_numbers_fails(self):
        with self.assertRaises(ValidationError):
            self.validator('John123')

    def test_name_with_symbols_fails(self):
        with self.assertRaises(ValidationError):
            self.validator('John@Doe')


class FileSizeValidatorTests(TestCase):
    def setUp(self):
        self.validator = FileSizeValidator(file_size=1)  # 1MB limit

    def test_small_file_passes(self):
        file = SimpleUploadedFile('photo.jpg', b'x' * 1024)  # 1KB
        try:
            self.validator(file)
        except ValidationError:
            self.fail('FileSizeValidator raised ValidationError on a small file')

    def test_large_file_fails(self):
        file = SimpleUploadedFile('photo.jpg', b'x' * (2 * 1024 * 1024))  # 2MB
        with self.assertRaises(ValidationError):
            self.validator(file)
