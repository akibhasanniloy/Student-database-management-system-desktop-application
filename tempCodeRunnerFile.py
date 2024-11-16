def validate_phone(phone_number):
    # Regular expression for Bangladeshi phone numbers
    phone_regex = r"^\+8801[3-9]\d{8}$"
    return re.match(phone_regex, phone_number)