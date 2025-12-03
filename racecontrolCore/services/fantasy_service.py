def prepare_fantasy_output(df):
    """
    df is already produced by the backend (Python list or list[dict]).
    This function ensures keys are named properly for the UI.
    """
    return [
        {
            "driver": row.get("driverId"),
            "fantasy_score": row.get("fantasy_score"),
        }
        for row in df
    ]