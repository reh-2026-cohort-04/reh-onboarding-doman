# Applicant Record Validator

A Python validator for the Rikai Day 00 onboarding exercise. It checks applicant records for required fields, correct types, and valid age and GPA ranges.

## Setup on Windows

Run these commands in PowerShell from the project folder. Use Python 3.11 or newer. This project was developed with Python 3.13.

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --group dev
.\.venv\Scripts\python.exe -m pre_commit install
```

## Usage

```python
from src.validator import RecordValidator

record = {
    "student_id": "S001",
    "full_name": "Jamie Tan",
    "age": 25,
    "gpa": 3.5,
    "skills": ["Python", "SQL"],
    "active": True,
}

validated_record = RecordValidator().validate(record)
```

The validator returns the record if it passes and raises `RecordValidationError` if a rule fails. Age must be an integer from 18 to 65, and GPA must be a float from 0.0 to 4.0. Both ranges include their endpoints. `configs/schema.json` documents all six fields.

## Verification

```powershell
.\.venv\Scripts\python.exe -m pytest -v
.\.venv\Scripts\python.exe -m ruff check src tests
.\.venv\Scripts\python.exe -m ruff format --check src tests
```