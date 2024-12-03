def is_safe(report):
    """
    Check if a report is safe based on the given rules.
    """
    increasing = True
    decreasing = True

    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        # Check if difference is within [1, 3]
        if not (1 <= abs(diff) <= 3):
            return False

        # Check for increasing or decreasing sequence
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False

    # The report is safe if it is either strictly increasing or decreasing
    return increasing or decreasing


def count_safe_reports(input_file):
    """
    Count the number of safe reports from the input file.
    """
    safe_count = 0

    with open(input_file, "r") as file:
        for line in file:
            # Parse the report as a list of integers
            report = list(map(int, line.split()))
            # Check if the report is safe
            if is_safe(report):
                safe_count += 1

    return safe_count


# Input file name
input_file = "input.txt"

# Calculate and print the number of safe reports
safe_reports = count_safe_reports(input_file)
print(f"Number of safe reports: {safe_reports}")