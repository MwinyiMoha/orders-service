from core.utils.functions import get_random_code


class TestCore:
    def test_get_random_code(self):
        code_1 = get_random_code(3)
        code_2 = get_random_code(15)

        assert len(code_1) == 3
        assert len(code_2) == 15
        assert code_1.isupper()
        assert code_2.isalnum()
