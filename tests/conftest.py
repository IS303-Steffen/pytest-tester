import pytest

@pytest.fixture
def sample_number():
    return 10

# Enter the file name, use the solution file when testing.
file_to_test = "a2_BMI_solution.py"

# This runs the script with optional user inputs. If inputs are provided, monkeypatch is used to mock them.
@pytest.fixture
def run_script(monkeypatch, capsys):
    def _run(user_inputs=None):
        # If user_inputs is provided, mock the input() function to return these inputs
        if user_inputs is not None:
            input_iter = iter(user_inputs)
            monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

        # Run the script
        with open(file_to_test) as f:
            code = compile(f.read(), file_to_test, 'exec')
            exec(code)

        # Capture the output
        captured = capsys.readouterr()

        print("Raw captured output (before split):", repr(captured.out))

        # Return the captured output as a list of strings
        return captured.out.strip().split('\n')
    
    return _run