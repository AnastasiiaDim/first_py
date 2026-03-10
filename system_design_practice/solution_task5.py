# Data Validation Pipeline

data = [
    {"id": 1, "value": 50},
    {"id": 2, "value": 120},
    {"id": 3},
    {"id": 4, "value": 30}
]

def is_valid_record(record):
    if not "value" in record:
        return False
    if record["value"] < 0 or record["value"] > 100:
        return False
    return True

def filter_valid_records(data_to_filter):
    valid_records = []
    for record in data_to_filter:
        if is_valid_record(record):
            valid_records.append(record)


