from example_function import add_5


def test_add_five(sample_number):
    assert add_5(3) == 8
    assert add_5(sample_number) == 15
    assert add_5(-5) == 0


# Override the built-in input to capture prompts
def mock_input(expected_prompts, inputs):
    """ Helper function to mock input and capture prompts """
    input_iter = iter(inputs)
    prompt_iter = iter(expected_prompts)

    def mocked_input(prompt):
        expected_prompt = next(prompt_iter)  # Store the next expected prompt
        assert prompt == expected_prompt, f"Expected: {expected_prompt}, but got: {prompt}"
        return next(input_iter)  # Return the next user input
    
    return mocked_input

# Test to verify correct prompts for user inputs
def test_correct_output_message(monkeypatch, run_script):
    # Expected input prompts
    expected_prompts = [
        "Give me an example input: ",
        "Give me an example input 2: "
    ]
    
    # Mock inputs that would be provided by the user
    user_inputs = ['Example 1', 'Example 2']

    # Patch the built-in input function with mock_input
    monkeypatch.setattr('builtins.input', mock_input(expected_prompts, user_inputs))

    # Run the script using the run_script fixture (it doesn't return output here)
    run_script()