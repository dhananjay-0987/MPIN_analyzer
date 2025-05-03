# utils/helpers.py

def generate_mpin_patterns(dob_self, dob_spouse, anniversary):
    """
    Generate all relevant 4‑digit and 6‑digit MPIN patterns
    from up to three dates in DD-MM-YYYY format.
    Returns a set of string patterns.
    """
    patterns = set()
    for date_str in (dob_self, dob_spouse, anniversary):
        if not date_str:
            continue

        dd, mm, yyyy = date_str.split('-')
        yy = yyyy[-2:]
        cc = yyyy[:2]

        # 4‑digit patterns
        patterns.update({
            dd + mm,      # ddmm
            mm + dd,      # mmdd
            yy + mm,      # yymm
            mm + yy,      # mmyy
            yy + dd,      # yydd
            dd + yy,      # ddyy
            yyyy         # full year, e.g. "1990"
        })

        # 6‑digit patterns
        patterns.update({
            dd + mm + yy,      # ddmmyy
            mm + dd + yy,      # mmddyy
            yy + mm + dd,      # yymmdd
            yy + dd + mm,      # yyddmm
            dd + mm + yyyy,    # ddmmyyyy (8-digit, ignored by 6‑digit analyzer)
            mm + dd + yyyy,    # mmddyyyy (8-digit)
            yyyy + mm + dd,    # yyyymmdd (8-digit)
            dd + mm + cc,      # ddmmCC
            mm + dd + cc,      # mmddCC
            cc + dd + mm,      # CCddmm
            yyyy + mm,         # yyyymm (6-digit year+month)
        })

    return patterns
