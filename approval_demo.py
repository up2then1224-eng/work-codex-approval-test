def clamp_percent(value):
    """Clamp an integer to the range 0 through 100."""
    return max(0, min(value, 100))
