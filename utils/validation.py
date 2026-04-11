from .logger import log
import os

def handleInvalidRows(df, condition, column, threshold, output_path):
    invalid_rows = df[condition].copy()
    invalid_rows_count = len(invalid_rows)
    total_df_len =  len(df)

    if total_df_len == 0:
        raise ValueError("Data set is empty.")
    
    ratio = invalid_rows_count/total_df_len

    if ratio > threshold:
        log.error(f"{column}: too many invalid rows({ratio:.2%})")
        raise ValueError(f"{column}: data quality is too low")
    
    elif (invalid_rows_count != 0):
        log.warning(f"{column}: Dropping {invalid_rows_count} invalid rows ({ratio:.2%})")
        
        #Adding reason
        invalid_rows['dropped_reason'] = column

        #save to a csv
        invalid_rows.to_csv(
            output_path,
            mode = 'a',
            index = False,
            header = not os.path.exists(output_path)
        )

    df = df[~condition]
    return df


class Validation:
    def __init__(self, rules, threshold, output_path):
        self.rules = rules
        self.threshold = threshold
        self.output_path = output_path

    def _parse_condition(self, df, column, condition_str):
        #Convert conditional string to actual panda condition
        
        condition_str = condition_str.strip()

        if "<=" in condition_str:
            value = float(condition_str.split('<=')[1].strip())
            return df[column] <= value
        elif ">=" in condition_str:
            value = float(condition_str.split('>=')[1].strip())
            return df[column] >= value
        elif "<" in condition_str:
            value = float(condition_str.split('<')[1].strip())
            return df[column] < value
        elif ">" in condition_str:
            value = float(condition_str.split('>')[1].strip())
            return df[column] > value
        elif "==" in condition_str:
            value = float(condition_str.split('==')[1].strip())
            return df[column] == value
        else:
            raise ValueError(f"Unsupported condition: {condition_str}")
        
    def apply_mapping(self, df, column, condition_str):
        # Handles mapping condition like: map:Yes=1,No=0

        mapping_str = condition_str.split(':')[1].strip()
        mapping = dict(item.split('=') for item in mapping_str.split(','))

        log.warning(f"Mapping values for column: {column}")

        df[column] = df[column].map(mapping).fillna(0)

        # Strict validation (no silent errors)
        # if df[column].isnull().any():
        #     raise ValueError(f"Invalid values found in column '{column}' during mapping")
        
        return df

    def clean(self,  df):         
        log.info('validation layer')
        initial_size = len(df)

        # 1. global null check
        if df.isnull().values.any():
            log.error('Null value exist in the dataset.')
            raise ValueError("Critical null value present.")
        
        for rule in self.rules:
            column = rule['column']
            condition_str = rule['condition']

            # Handle map seperately
            if condition_str.startswith('map'):
                df = self.apply_mapping(df, column, condition_str)
                continue

            # Parse condition dynamically
            condition = self._parse_condition(df, column, condition_str)

            df = handleInvalidRows(
                df, 
                condition, 
                column, 
                self.threshold,
                self.output_path
            )

        # Final drop rate check
        final_size = len(df)

        if initial_size == 0:
            raise ValueError("Initial dataset is empty")
        
        drop_rate = (initial_size - final_size) / initial_size

        log.info(f"Total rows dropped: {initial_size - final_size}")
        log.info(f"Drop rate: {drop_rate:.2%}")
        log.info(f"Threshold: {self.threshold:.2%}")

        if drop_rate > self.threshold:
            log.error("Overall drop rate exceeded threshold. Pipeline stopped.")
            raise ValueError("Too many rows dropped overall")

        log.info("Validation completed successfully")

        return df
        