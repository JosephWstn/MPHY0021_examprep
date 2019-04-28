import pytest
from pytest import raises
from simplemaths import SimpleMaths as sm

class TestSimpleMaths():
    
    # negative test on constructor for a float
    def test_const_neg_1(self):
        test_value = 2.5
        with raises(ValueError) as exception:
            sm_obj = sm(test_value)
    
    # negative test on constructor for a string
    def test_const_neg_2(self):
        test_value = "string"
        with raises(ValueError) as exception:
            sm_obj = sm(test_value)
    
    # positive test on constructor testing it correctly assigns the number value
    def test_const_pos(self):
        test_value = 80
        sm_obj = sm(test_value)
        assert(sm_obj.number == test_value)
        
    # negative test on factorial for negative number
    def test_fact_neg(self):
        test_value = -3
        sm_obj = sm(test_value)
        with raises(RuntimeError) as exception:
            sm_obj.factorial()
    
    # positive test for factorial
    def test_fact_pos(self):
        test_value = 3
        test_result = 6
        sm_obj = sm(test_value)
        assert(sm_obj.factorial() == test_result)
        
    # positive test for square
    def test_square_pos(self):
        test_value = 3
        test_result = 9
        sm_obj = sm(test_value)
        assert(sm_obj.square() == test_result)
        
    # positive test for power using default argument
    def test_power_def(self):
        test_value = 3
        test_result = 27
        sm_obj = sm(test_value)
        assert(sm_obj.power() == test_result)
        
    # positive test for power reassigning default argument
    def test_power_nondef(self):
        test_value = 2
        power = 4
        test_result = 16
        sm_obj = sm(test_value)
        assert(sm_obj.power(power) == test_result)
        
    # test odd/even test for 0
    def test_o_e_zero(self):
        test_value = 0
        test_result = "Even"
        sm_obj = sm(test_value)
        assert(sm_obj.odd_or_even() == test_result)
        
    # test odd/even test for odd
    def test_o_e_odd(self):
        test_value = 1
        test_result = "Odd"
        sm_obj = sm(test_value)
        assert(sm_obj.odd_or_even() == test_result)
        
    # test odd/even test for even
    def test_o_e_even(self):
        test_value = 8
        test_result = "Even"
        sm_obj = sm(test_value)
        assert(sm_obj.odd_or_even() == test_result)
        
    # test odd/even test for even -ve
    def test_o_e_even_neg(self):
        test_value = -8
        test_result = "Even"
        sm_obj = sm(test_value)
        assert(sm_obj.odd_or_even() == test_result)
        
    # test odd/even test for odd -ve
    def test_o_e_odd_neg(self):
        test_value = -9
        test_result = "Odd"
        sm_obj = sm(test_value)
        assert(sm_obj.odd_or_even() == test_result)
        
    # positive test for square root
    def test_sqrt_pos(self):
        test_value = 9
        test_result = 3
        sm_obj = sm(test_value)
        assert(sm_obj.square_root() == test_result)
        
    # negative test for square root
    def test_sqrt_neg(self):
        test_value = -9
        sm_obj = sm(test_value)
        with raises(ValueError) as exception:
            sm_obj.square_root()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        