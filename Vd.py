from typing import Tuple, Dict

def is_valid_email_address(email_addr: str) -> bool:
    if email_addr.count('@') != 1:
        return False
    if len(email_addr) > 254:
        return False
    local_part, domain_part = email_addr.split('@')
    if len(local_part) > 64 or len(local_part) == 0:
        return False
    if len(domain_part) > 251 or len(domain_part) == 0:
        return False

    for char in email_addr:
        if char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.@':
            return False

    if domain_part.count('.') != 1:
        return False

    if local_part[0] in '.-' or local_part[-1] in '-.':
        return False

    if email_addr[-4:] not in ['.com', '.net', '.org']:
        return False

    return True

def validate_email_payload(sender_name: str, sender_addr: str, receiver_name: str, receiver_addr: str, html: str, replacements: Dict):
    sender_name = sender_name.strip()
    receiver_name = receiver_name.strip()

    if not (5 <= len(sender_name) <= 30):
        raise ValueError("Sender name is not valid")

    if not (5 <= len(receiver_name) <= 60):
        raise ValueError("Receiver name is not valid")

    sender_addr = sender_addr.strip()
    receiver_addr = receiver_addr.strip()

    if not is_valid_email_address(sender_addr):
        raise ValueError("Sender email address is not valid")

    if not is_valid_email_address(receiver_addr):
        raise ValueError("Receiver email address is not valid")

    for key, value in replacements.items():
        if not value:
            continue
        if f'{{{key}}}' not in html:
            raise ValueError("HTML doesn't contain the key")
        html = html.replace(f'{{{key}}}', value)

    if '{' in html:
        raise ValueError("HTML contains surplus placeholders")

    return True
