from utils.analyzer_4digit import FourDigitMPINAnalyzer
from utils.analyzer_6digit import SixDigitMPINAnalyzer

def main():
    print("MPIN Strength Analyzer\n")
    
    mpin = input("Enter your MPIN: ").strip()
    dob_self = input("Enter your DOB (DD-MM-YYYY) or leave blank: ").strip() or None
    dob_spouse = input("Enter Spouse's DOB (DD-MM-YYYY) or leave blank: ").strip() or None
    anniversary = input("Enter Anniversary Date (DD-MM-YYYY) or leave blank: ").strip() or None

    if len(mpin) == 4:
        analyzer = FourDigitMPINAnalyzer(mpin, dob_self, dob_spouse, anniversary)
    elif len(mpin) == 6:
        analyzer = SixDigitMPINAnalyzer(mpin, dob_self, dob_spouse, anniversary)
    else:
        print("\n Invalid MPIN length. Only 4 or 6 digits allowed.")
        return

    result = analyzer.analyze()
    
    print("\n MPIN Analysis Result:")
    print(f"Strength: {result['strength']}")
    if result["reasons"]:
        print("Reasons:")
        for reason in result["reasons"]:
            print(f" - {reason}")
    else:
        print("No weaknesses detected.")

if __name__ == "__main__":
    main()
