import pytest
from app import app as flask_app
from app.app import nltk_summarizer

@pytest.fixture
#testing functions
def add():
    pass
    

# def test_output_list():
#     query = "imran Khan"
#     results = flask_app.search_index(query)

#     assert isinstance (results,list)
#     assert len(results) <= 10

def test1_nltk_summarizer():
    input_text = "This is a sample text for summarization. It should produce a concise summary."
    expected_text = "This is a sample text"

    actual_text = nltk_summarizer(input_text)

    assert actual_text == expected_text
