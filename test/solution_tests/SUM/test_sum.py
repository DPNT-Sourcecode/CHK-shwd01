
import sys
print(sys.path)
from lib.solutions.SUM import sum_solution
class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
        assert sum_solution.compute(3, 2) == 5
        assert sum_solution.compute(3, 1) == 5 #wrong test; let's see what happens


