from src.diego_m_calculator_pkg.calculator import generate_plot_data
import numpy as np

# test the generate_plot_data function
def test_generate_plot_data():
    function = "x^2 + 2x + 1"
    x_range = (-5,5)
    step = 0.2
    expected_x_vals = np.arange(x_range[0], x_range[1], step)
    expected_y_vals = expected_x_vals**2 + 2*expected_x_vals + 1
    x_vals, y_vals = generate_plot_data(function, x_range,step)
    assert np.allclose(x_vals, expected_x_vals)
    assert np.allclose(y_vals, expected_y_vals)




