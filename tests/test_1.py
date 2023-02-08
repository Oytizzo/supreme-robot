# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        # assert hasattr(x, "check")
        assert "h" in x

    def test_three(self):
        x = "this"
        assert "h" in x

    def test_four(self):
        x = "hello"
        assert hasattr(x, "check")
        # assert "h" in x

    def test_five(self):
        x = "this"
        assert "h" in x

    def test_six(self):
        x = "hello"
        # assert hasattr(x, "check")
        assert "h" in x
