def validate_date(date_str):
    from datetime import datetime
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def handle_error(error_message):
    print(f"Error: {error_message}")

def format_review_data(title, description, date, reviewer_name, rating):
    return {
        "title": title,
        "description": description,
        "date": date,
        "reviewer_name": reviewer_name,
        "rating": rating
    }