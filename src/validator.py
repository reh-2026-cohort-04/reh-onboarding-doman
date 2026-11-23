"""Validate applicant records before they enter the data pipeline."""

import logging
from typing import Any

logger = logging.getLogger(__name__)


class RecordValidationError(ValueError):
    """Raised when an applicant record fails validation."""


class RecordValidator:
    """Check that an applicant record meets the required schema."""

    def validate(self, record: dict[str, Any]) -> dict[str, Any]:
        """Return the valid record or raise RecordValidationError."""
        if not isinstance(record, dict):
            raise RecordValidationError("Record must be a dictionary.")

        required_fields = ("student_id", "full_name", "age", "gpa", "skills", "active")
        for field in required_fields:
            if field not in record:
                raise RecordValidationError(f"Missing required field: {field}.")

        for field in ("student_id", "full_name"):
            value = record[field]
            if not isinstance(value, str) or not value.strip():
                raise RecordValidationError(f"{field} must be a non-empty string.")

        age = record["age"]
        if type(age) is not int or not 18 <= age <= 65:
            raise RecordValidationError("age must be an integer from 18 to 65.")

        gpa = record["gpa"]
        if not isinstance(gpa, float) or not 0.0 <= gpa <= 4.0:
            raise RecordValidationError("gpa must be a float from 0.0 to 4.0.")

        skills = record["skills"]
        if not isinstance(skills, list) or not all(
            isinstance(skill, str) for skill in skills
        ):
            raise RecordValidationError("skills must be a list of strings.")

        if not isinstance(record["active"], bool):
            raise RecordValidationError("active must be a boolean.")

        if age <= 19 or age >= 64:
            logger.warning("Applicant age is near a validation boundary: %s", age)

        if gpa <= 0.1 or gpa >= 3.9:
            logger.warning("Applicant GPA is near a validation boundary: %s", gpa)

        logger.info("Applicant record passed validation.")
        return record
