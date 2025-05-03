from datetime import datetime
from .helpers import generate_mpin_patterns
class SixDigitMPINAnalyzer:
    COMMON_MPINS = [
        "123456", "000000", "111111", "121212", "654321",
        "222222", "333333", "444444", "555555", "666666",
        "777777", "888888", "999999"
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
                dd + mm + yy,
                dd + mm + yyyy,
                mm + dd + yy,
                mm + dd + yyyy,
                yy + mm + dd,
                yyyy + mm + dd,
                yy + dd + mm,
                dd + yy + mm,
                mm + yy + dd,
                yyyy[-2:] + mm + dd
                }
        except Exception:
            return set()

    def analyze(self):
        reasons = []
        if self.mpin in self.COMMON_MPINS:
            reasons.append("COMMONLY_USED")
        # Generate all date‑based patterns and check only 6‑digit ones 
        date_patterns = generate_mpin_patterns(*self.dates)
        six_digit_patterns = {p for p in date_patterns if len(p) == 6}

        if self.mpin in six_digit_patterns:
            labels = ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY"]
            for date_str, label in zip(self.dates, labels):
                if date_str and self.mpin in generate_mpin_patterns(date_str, date_str, date_str):
                    reasons.append(label)
                    break
        strength = "WEAK" if reasons else "STRONG"
        return {"strength": strength, "reasons": reasons}
