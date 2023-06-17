from hello_world import index
def test_my_function():
    assert index.handler(None, None) == "1234"
