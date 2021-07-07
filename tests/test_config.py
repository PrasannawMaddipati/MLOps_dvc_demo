import pytest


class NotinRange(Exception):
    def __init__(self,message = "value not in range"):
        self.message = message
        super().__init__(self.message)

def test_generic():
    a =2
    with pytest.raises(NotinRange):
        if a not in range(10,20):
            raise NotinRange
    