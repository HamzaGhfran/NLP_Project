import pytest
from app import app as flask_app

@pytest.fixture
def test_nltk_summarizer():
    input_text = "This is a sample text for summarization. It should produce a concise summary."
    expected_text = "This is a sample text"

    actual_text = flask_app.nltk_summarizer(input_text)

    assert actual_text == expected_text

def test_output_list():
    query = "imran Khan"
    results = flask_app.search_index(query)

    assert isinstance (results,list)
    assert len(results) <= 10
