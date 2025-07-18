import pytest
from neurolingo_demo import NeuroLingoEngine

def test_engine_initialization():
    """Test that the engine initializes correctly."""
    engine = NeuroLingoEngine()
    assert engine is not None
    assert len(engine.vocab) > 0

def test_generation():
    """Test basic generation functionality."""
    engine = NeuroLingoEngine()
    sample = engine.generate("⚡", max_length=5)
    assert isinstance(sample, str)
    assert len(sample) > 0

# Add more tests as needed
