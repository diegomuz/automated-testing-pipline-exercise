from src.diego_m_calculator_pkg.calculator import handle_special_notations

# tests the handle_special_notations function

""""
def test_handle_special_notations_power():
    assert handle_special_notations("y = x^2") == "x**2"
def test_handle_special_notations_colon():
    assert handle_special_notations("y = 2:3") == "2/3"
def test_handle_special_notations_word_number_before_x():
    assert handle_special_notations("y = 2x") == "2*x"
    assert handle_special_notations("y = 2 x") == "2*x"
    assert handle_special_notations("y = 2(x)") == "2*(x)"
    assert handle_special_notations("y = sin(2x)") == "sin(2*x)"
def test_handle_special_notations_word_number_after_x():
    assert handle_special_notations("y = x2") == "x*2"
    assert handle_special_notations("y = x 2") == "x*2"
    assert handle_special_notations("y = (x)2") == "(x)*2"
    assert handle_special_notations("y = sin(x)2") == "sin(x)*2"
    assert handle_special_notations("y = sin(x)x") == "sin(x)*x"
def test_handle_special_notations_parenthesis():
    assert handle_special_notations("y = (x)(x)") == "(x)*(x)"
    assert handle_special_notations("y = (x) (x)") == "(x)*(x)"


"""
