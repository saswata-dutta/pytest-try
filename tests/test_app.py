
from testutils import compare
from myapp import app


def test_hello():
    compare(app.hello(), "hello world")
