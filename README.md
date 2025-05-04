## MPIN Strength Analyzer

This file contains a comprehensive solution for analyzing 4‑digit and 6‑digit MPINs (Mobile Personal Identification Numbers) to determine their strength and detect easily guessable or demographic‑based PINs.

---

## Problem Statement

Users often choose easily guessable MPINs when accessing mobile banking apps. These PINs may be:

1. **Commonly used** patterns (e.g., `1234`, `0000`, `123456`, etc.).  
2. **Based on user demographics**, such as:  
   - Date of Birth (self)  
   - Date of Birth (spouse)  
   - Wedding Anniversary  

A robust solution must:  
- Identify weak MPINs caused by common patterns.  
- Identify weak MPINs derived from demographic information.  
- Provide meaningful reasons for why a PIN is considered weak.

---

##  Approach 

1. **Modular Design**  
   - `utils/` contains two analyzer classes:  
     - `FourDigitMPINAnalyzer` (4‑digit logic)  
     - `SixDigitMPINAnalyzer` (6‑digit logic)  
     - `helpers.py` generates all possible MPIN patterns based on up to three dates.
   - `main.py` entry point for running MPIN analysis interactively via CLI.
   - `test_cases` contains two file:
     - `test_runner.py` automated test executor that reads JSON test data and validates outputs.
     - `test_data.json` contains structured test case inputs and expected outputs.

2. **Pattern Generation**  
   - Common lists for 4-digit and 6‑digit MPINs.  
   - Demographic patterns (permutations of `dd`, `mm`, `yy`, `yyyy`, and century prefix `cc`).

3. **Analysis Flow**  
   - Check common list → if match, append `COMMONLY_USED`.  
   - Generate patterns via helper and filter by length (4 or 6) → if match, identify which date produced it and append the appropriate `DEMOGRAPHIC_*` label.

4. **Result**  
   - An object with `WEAK` and a `reasons` array, and `STRONG` with a `empty` array.

---

##  Requirements

- Python 3.x version
- No external libraries are required.

---

##  How to run 
  - To run main file type command:
  ` python3 main.py ` 
  - To run test cases type command:
  ` python3 test_cases/test_runner.py `

