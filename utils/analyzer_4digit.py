from datetime import datetime

class FourDigitMPINAnalyzer:
    COMMON_MPINS = [
        "0000", "1111", "1234", "1212", "1122", "2222",
        "3333", "4444", "5555", "6666", "7777", "8888", "9999",
        "4321", "1010", "2000", "1230", "1100"
    ]

    def __init__(self, mpin: str, dob_self=None, dob_spouse=None, anniversary=None):
        self.mpin = mpin
        self.dob_self = dob_self
        self.dob_spouse = dob_spouse
        self.anniversary = anniversary

    def _extract_date_patterns(self, date_str: str):
        try:
            dt = datetime.strptime(date_str, "%d-%m-%Y")
            dd = dt.strftime("%d")
            mm = dt.strftime("%m")
            yy = dt.strftime("%y")
            yyyy = dt.strftime("%Y")

            return {
                dd + mm, mm + dd, yy + mm, mm + yy,
                yyyy[:2] + mm, mm + yyyy[:2],
                yy + yy, yyyy[-2:] + mm
            }
        except Exception:
            return set()

    def analyze(self):
        reasons = []

        if self.mpin in self.COMMON_MPINS:
            reasons.append("COMMONLY_USED")

        if self.dob_self and self.mpin in self._extract_date_patterns(self.dob_self):
            reasons.append("DEMOGRAPHIC_DOB_SELF")
        if self.dob_spouse and self.mpin in self._extract_date_patterns(self.dob_spouse):
            reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
        if self.anniversary and self.mpin in self._extract_date_patterns(self.anniversary):
            reasons.append("DEMOGRAPHIC_ANNIVERSARY")

        strength = "WEAK" if reasons else "STRONG"
        return {"strength": strength, "reasons": reasons}
