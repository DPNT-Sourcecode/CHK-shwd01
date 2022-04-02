from lib.solutions.CHK import checkout_solution
class TestSum():
    def test_sum(self):
        assert checkout_solution("AAAAAv") == -1
        assert checkout_solution.compute("A") == 50
        assert checkout_solution.compute("B") == 30
        assert checkout_solution.compute("AAA") == 180
        assert checkout_solution.compute("BDBZ") == -1
        assert checkout_solution.compute("BDB") == 60

