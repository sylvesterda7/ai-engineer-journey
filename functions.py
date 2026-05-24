def calculate_study_time(hours_per_day, days):
    total = days * hours_per_day
    return total

def check_readiness(hours):
    if hours >= 300:
        return "Job ready - start applying"
    elif hours >= 150:
        return "Building strong foundations"
    elif hours >= 50:
        return "Good progress - keep going"
    else:
        return "Just getting started - stay consistent"
    
def print_report(name, days, hours_per_day):
    total = calculate_study_time(hours_per_day, days)
    status = check_readiness(total)
    print("--- Progress Report ---")
    print(f"Name: {name}")
    print(f"Days studied: {days}")
    print(f"Hours per day: {hours_per_day}")
    print(f"Total study time: {total} hours")
    print(f"Readiness status: {status}")
    print("--- End of Report ---")

print_report("Sylvester", 190, 3)