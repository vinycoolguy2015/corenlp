from nlplogic.corenlp import get_phrases

import nltk
nltk.download('punkt_tab')

def test_get_phrase():
    assert "golden state" in get_phrases("Golden State Warriors")
