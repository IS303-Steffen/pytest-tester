import re
import importlib
import pytest

def normalize_text(text):
    # Remove punctuation, extra spaces, and make it lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower().strip()          # Lowercase and remove leading/trailing spaces
    text = ' '.join(text.split())        # Normalize spaces
    return text


def test_multiple_output(capsys, monkeypatch):

    # The list of prompts (what the input() function should display)
    expected_input_prompts = ["Enter some text 1: ",
                              "Enter some text 2: "]

    # corresponding inputs for the test (Examples of what the user could enter)
    simulated_inputs = ["Example input response 1",
                        "Example input response 2"]

    # what the print() function should display
    expected_outputs = ["This is the first output.",
                        "This is the second output.",
                        "This is the third output.",
                        "the first output Example input response 1",
                        "the second output Example input response 2"]
    
    # Create an iterator over the list of simulated inputs
    input_iter = iter(simulated_inputs)

    # List to capture the prompts passed to input()
    captured_prompts = []

    # this is a replacement for the actual input() method.
    # monkeypatch will replace input() with mock_input() in the student's file
    # that way it can run without actually waiting for input in the terminal.
    # the prompt parameter will receive whatever was inputted into the original input() function.
    def mock_input(prompt):
        captured_prompts.append(prompt)
        return next(input_iter) # grabs the next thing from the simulated inputs list

    monkeypatch.setattr('builtins.input', mock_input)

    import example_function
    importlib.reload(example_function)
    # Capture the output from the print statements
    captured = capsys.readouterr().out
    
    # Now validate the input prompts that were captured
    assert captured_prompts == expected_input_prompts, (
        f"Expected prompts: {expected_input_prompts}, but got: {captured_prompts}"
    )

    # Split the captured output into lines (in case there are multiple print statements)
    output_lines = captured.strip().splitlines()

    # Check if the number of lines matches the expected outputs
    assert len(output_lines) == len(expected_outputs), "The number of printed statements is incorrect."

    # Compare each output line individually with the normalized expected output
    for i, expected in enumerate(expected_outputs):
        assert normalize_text(output_lines[i]) == normalize_text(expected), f"\n\nPrinted output #{i+1} wasn't the expected result:"