from datetime import datetime
from .helpers import generate_mpin_patterns
class FourDigitMPINAnalyzer:
    COMMON_MPINS = [
        "0000", "1111", "1234", "1212", "1122", "2222",
        "3333", "4444", "5555", "6666", "7777", "8888", "9999",
        "4321", "1010", "2000", "1230", "1100"
    ]

    def __init__(self, mpin: str, dob_self=None, dob_spouse=None, anniversary=None):
        self.mpin = mpin
        self.dates = (dob_self, dob_spouse, anniversary)

    def _extract_date_patterns(self, date_str: str):
        try:
            dt = datetime.strptime(date_str, "%d-%m-%Y")
            dd = dt.strftime("%d")
            mm = dt.strftime("%m")
            yy = dt.strftime("%y")
            yyyy = dt.strftime("%Y")
            return {
                dd + mm, mm + dd,
                yy + mm, mm + yy,
                yy + dd, dd + yy,
                yyyy[-2:] + mm, mm + yyyy[-2:],
                dd + yy, yy + dd
                }
        except Exception:
            return set()

    def analyze(self):
        reasons = []
        if self.mpin in self.COMMON_MPINS:
            reasons.append("COMMONLY_USED")
        # Generate all date‑based patterns and check only 6‑digit ones 
        date_patterns = generate_mpin_patterns(*self.dates)
        four_digit_patterns = {p for p in date_patterns if len(p) == 4}
        if self.mpin in four_digit_patterns:
            labels = ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY"]
            for date_str, label in zip(self.dates, labels):
                if date_str and self.mpin in generate_mpin_patterns(date_str, date_str, date_str):
                    reasons.append(label)
                    break
        strength = "WEAK" if reasons else "STRONG"
        return {"strength": strength, "reasons": reasons}

