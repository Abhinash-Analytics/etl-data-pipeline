from .cleaning import (
    HandleIntegerMissingValues,
    DropNull,
    DropColumn,
    Encoding
)

class TransformationFactory:
    
    @staticmethod
    def build(changes_config, full_config):
        transformation = []

        for steps in changes_config:
            step_type = steps['type']

            if step_type == 'HandleIntegerMissingValues':
                transformation.append(
                    HandleIntegerMissingValues(
                        steps['column'], 
                        full_config['validation']['missing_values']['replace_with_nan']
                        )
                )
            elif step_type == 'DropNull':
                transformation.append(DropNull())
            elif step_type == 'DropColumn':
                transformation.append(DropColumn(steps['column']))
            elif step_type == 'Encoding':
                transformation.append(Encoding())
            else:
                raise ValueError(f"unknown change type: {step_type}")
            
        return transformation