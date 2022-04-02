from lib.solutions.CHK import checkout_solution
class TestSum():
    def test_sum(self):
        assert checkout_solution("AAAAAv") == -1
        assert checkout_solution.compute("A") == 50
        assert checkout_solution.compute("B") == 30
        assert checkout_solution.compute("AAA") == 180
        assert checkout_solution.compute("BDBZ") == -1
        assert checkout_solution.compute("BDB") == 60
        assert checkout("AAA")==130
        
        assert checkout("AAAAAA")==250
        assert checkout("AAAAA")==200
        assert checkout("AA")==100
        assert checkout("BB")==45
        assert checkout("B")==30
        assert checkout("bBB")==-1
        assert checkout("BBBBB")==120
        assert checkout("EEB")==80

        assert checkout("EE")==80
        assert checkout("BEBE")==110