from .cleaning import (
    HandleIntegerMissingValues,
    DropNull,
    DropColumn,
    Encoding
)
from transformation.standardize_columns import StandardizeColumns
from .to_numeric import ToNumeric


# Registry (replaces if-else)
TRANSFORMATION_MAP = {
    "StandardizeColumns": StandardizeColumns,
    "ToNumeric": ToNumeric,
    "HandleIntegerMissingValues": HandleIntegerMissingValues,
    "DropNull": DropNull,
    "DropColumn": DropColumn,
    "Encoding": Encoding
}


class TransformationFactory:

    @staticmethod
    def build(changes_config, full_config):
        transformations = []

        for step in changes_config:
            step_type = step.get('type')

            # Validate step type
            if not step_type:
                raise ValueError("Missing 'type' in transformation config")

            # Get class from map
            cls = TRANSFORMATION_MAP.get(step_type)

            if not cls:
                raise ValueError(f"Unknown transformation type: {step_type}")

            # Handle special case (needs extra config)
            if step_type == "HandleIntegerMissingValues":
                transformations.append(
                    cls(
                        step['column'],
                        full_config['validation']['missing_values']['replace_with_nan']
                    )
                )

            # 🔹 Transformations with column parameter
            elif 'column' in step:
                transformations.append(cls(step['column']))

            # 🔹 Transformations without parameters
            else:
                transformations.append(cls())

        return transformations