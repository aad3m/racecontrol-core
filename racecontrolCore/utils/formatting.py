from datetime import datetime

def format_next_race_when(local_date_str: str | None) -> str:
    if not local_date_str:
        return "TBA"
    # Just echo the string for now; can be improved to proper tz handling
    return local_date_str