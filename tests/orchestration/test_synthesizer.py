import pytest
from ambiance.orchestration.synthesizer import ResponseSynthesizer

def test_synthesize_markdown_removal():
    synth = ResponseSynthesizer()
    raw = "Here is **bold** and *italic* text."
    expected = "Here is bold and italic text."
    assert synth.synthesize(raw) == expected

def test_synthesize_code_block():
    synth = ResponseSynthesizer()
    raw = "Here is code:\n```python\nprint('hello')\n```\nDone."
    expected = "Here is code: [Code Block] Done."
    assert synth.synthesize(raw) == expected

def test_synthesize_headers():
    synth = ResponseSynthesizer()
    raw = "# Header 1\n## Header 2\nContent."
    expected = "Header 1 Header 2 Content."
    assert synth.synthesize(raw) == expected

def test_synthesize_links():
    synth = ResponseSynthesizer()
    raw = "Check [Google](https://google.com)."
    expected = "Check Google."
    assert synth.synthesize(raw) == expected

