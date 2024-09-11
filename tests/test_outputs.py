import re
import importlib

def normalize_text(text):
    # Remove punctuation, extra spaces, and make it lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower().strip()          # Lowercase and remove leading/trailing spaces
    text = ' '.join(text.split())        # Normalize spaces
    return text

def test_multiple_output(capsys):
    # Import the student's script which will execute the top-level code
    importlib.import_module("student_script")
    
    # Capture the output from the print statements
    captured = capsys.readouterr().out
    
    # Split the captured output into lines (in case there are multiple print statements)
    output_lines = captured.strip().splitlines()

    # Define the expected outputs in the correct order
    expected_outputs = [
        "this is the first output",
        "here is the second output",
        "finally the third output"
    ]

    # Check if the number of lines matches the expected outputs
    assert len(output_lines) == len(expected_outputs), "The number of printed statements is incorrect."

    # Compare each output line individually with the normalized expected output
    for i, expected in enumerate(expected_outputs):
        assert normalize_text(output_lines[i]) == normalize_text(expected), f"Mismatch at line {i+1}"