from datetime import datetime

class SixDigitMPINAnalyzer:
    COMMON_MPINS = [
        "123456", "000000", "111111", "121212", "654321",
        "222222", "333333", "444444", "555555", "666666",
        "777777", "888888", "999999"
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
                dd + mm + yy,
                dd + mm + yyyy,
                yyyy + mm,
                mm + yyyy,
                yy + mm + dd,
                mm + dd + yy
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
