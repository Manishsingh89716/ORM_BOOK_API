"""unit tests for business logic functions"""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from main import format_book_description

def test_format_book_description():
    """test book description formatter"""
    result = format_book_description("The Alchemist", "Paulo Coelho")
    #this matches the current helper function output
    assert result == "The Alchemist is written by Paulo Coelho"