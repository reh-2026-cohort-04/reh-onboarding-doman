import pytest

from src.validator import RecordValidationError, RecordValidator


@pytest.fixture
def sample_valid_record():
    return {
        "student_id": "S001",
        "full_name": "Jamie Tan",
        "age": 25,
        "gpa": 3.5,
        "skills": ["Python", "SQL"],
        "active": True,
    }


def test_valid_record_passes(sample_valid_record):
    assert RecordValidator().validate(sample_valid_record) == sample_valid_record


def test_missing_required_field_raises_error(sample_valid_record):
    del sample_valid_record["student_id"]

    with pytest.raises(RecordValidationError, match="student_id"):
        RecordValidator().validate(sample_valid_record)


@pytest.mark.parametrize("age", [17, 66])
def test_invalid_age_boundary_raises_error(sample_valid_record, age):
    sample_valid_record["age"] = age

    with pytest.raises(RecordValidationError, match="age"):
        RecordValidator().validate(sample_valid_record)


@pytest.mark.parametrize("gpa", [-0.1, 4.1])
def test_invalid_gpa_range_raises_error(sample_valid_record, gpa):
    sample_valid_record["gpa"] = gpa

    with pytest.raises(RecordValidationError, match="gpa"):
        RecordValidator().validate(sample_valid_record)


@pytest.mark.parametrize("skills", ["Python", ["Python", 42]])
def test_skills_type_validation(sample_valid_record, skills):
    sample_valid_record["skills"] = skills

    with pytest.raises(RecordValidationError, match="skills"):
        RecordValidator().validate(sample_valid_record)


@pytest.mark.parametrize(
    ("field", "value"),
    [("age", 18), ("age", 65), ("gpa", 0.0), ("gpa", 4.0)],
)
def test_exact_limits_pass(sample_valid_record, field, value):
    sample_valid_record[field] = value

    assert RecordValidator().validate(sample_valid_record) == sample_valid_record
