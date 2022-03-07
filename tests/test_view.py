
from testutils import compare
from myapp import view

def test_hello():
    compare(view.world(), "world")
