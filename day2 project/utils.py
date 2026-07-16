def capitalize_name(name: str) -> str:
    """Return the name in title case."""
    return name.title()


def calculate_percentage(score: int, total: int) -> float:
    """Return the percentage score."""
    return (score / total) * 100


def print_heading(title: str) -> None:
    """Print a formatted heading."""
    print(f"\n=== {title} ===")

print_heading("Student Report")

print(capitalize_name("ammu"))

print(calculate_percentage(450, 500))