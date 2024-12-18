from nlplogic.corenlp import get_phrases
import nltk
nltk.download('punkt')


def test_get_phrase():
    assert "golden state" in get_phrases("Golden State Warriors")
