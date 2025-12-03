def select_patients(patients, k):
    """
    Select up to k patient names in the order they should be called.

    Priority rules:
      1. Lower severity number first.
      2. If severity ties, lower arrival_order first.
    """

    if k == 0 or not patients:
        return []

    # Sort patients by (severity, arrival_order)
    sorted_patients = sorted(
        patients,
        key=lambda p: (p["severity"], p["arrival_order"])
    )

    # Select first k names
    return [p["name"] for p in sorted_patients[:k]]
