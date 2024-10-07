import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.codecaesar import chiffrement, dechiffrement

def test_chiffrement():
    assert chiffrement("ABC", 3) == "DEF"
    assert chiffrement("zab", 1) == "abc"
    assert chiffrement("Bonjour c'est le couillon de l'autre jour", 4) == "Fsrnsyv g'iwx pi gsymppsr hi p'eyxvi nsyv"
    assert chiffrement("!", 5) == "!"
    
    
def test_dechiffrement():
    assert dechiffrement("DEF", 3) == "ABC"
    assert dechiffrement("bcd", 1) == "abc"
    assert dechiffrement("Fsrnsyv g'iwx pi gsymppsr hi p'eyxvi nsyv", 4) == "Bonjour c'est le couillon de l'autre jour"
    assert dechiffrement("!", 5) == "!"