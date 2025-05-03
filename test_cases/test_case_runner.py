import json
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.analyzer_4digit import FourDigitMPINAnalyzer
from utils.analyzer_6digit import SixDigitMPINAnalyzer

# Known reason categories supported by analyzers
KNOWN_REASONS = {
    "COMMONLY_USED",
    "DEMOGRAPHIC_DOB_SELF",
    "DEMOGRAPHIC_DOB_SPOUSE",
    "DEMOGRAPHIC_ANNIVERSARY"
}

def load_test_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def run_test_case(test_case, index):
    mpin = test_case["mpin"]
    dob_self = test_case.get("dob_self")
    dob_spouse = test_case.get("dob_spouse")
    anniversary = test_case.get("anniversary")
    expected_strength = test_case["expected_strength"]
    expected_reasons = set(test_case["expected_reasons"])

    # Check for unknown reasons
    unknown_reasons = expected_reasons - KNOWN_REASONS
    if unknown_reasons:
        print(f"Test {index} Warning: Unknown expected reasons: {list(unknown_reasons)}")

    # Initialize appropriate analyzer
    if len(mpin) == 4:
        analyzer = FourDigitMPINAnalyzer(mpin, dob_self, dob_spouse, anniversary)
    elif len(mpin) == 6:
        analyzer = SixDigitMPINAnalyzer(mpin, dob_self, dob_spouse, anniversary)
    else:
        print(f"Test {index}: Invalid MPIN length.")
        return False

    result = analyzer.analyze()
    actual_strength = result["strength"]
    actual_reasons = set(result["reasons"])

    # Evaluate test outcome
    if actual_strength == expected_strength and actual_reasons == expected_reasons:
        print(f" Test {index} Passed")
        return True
    else:
        print(f"Test {index} Failed")
        print("   Input MPIN:", mpin)
        print("   Expected:", expected_strength, list(expected_reasons))
        print("   Got     :", actual_strength, list(actual_reasons))
        return False

def main():
    test_data = load_test_data("test_cases/test_data.json")
    total = len(test_data)
    passed = sum(run_test_case(tc, idx + 1) for idx, tc in enumerate(test_data))
    print(f"\n Test Summary: {passed}/{total} tests passed.")

if __name__ == "__main__":
    main()
