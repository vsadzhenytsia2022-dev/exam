def validate_email(email: str) -> bool:
    """Примітивна перевірка наявності @ та крапки після неї."""
    if "@" in email:
        at_index = email.find("@")
        if "." in email[at_index + 1:]:
            return True
    return False

if __name__ == "__main__":
    email = "test@example.com"
    result = validate_email(email)
    print(f"Результат перевірки: {result}")