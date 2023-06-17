from hello_world import index
def test_my_function():
    assert index.handler(None, None) == "42: answer for 42 is 42"
