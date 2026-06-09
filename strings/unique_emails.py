from typing import List


def unique_email_addresses(emails: List[str]) -> int:
    unique_emails = set()

    for email in emails:
        normalized_email = []

        for index, string in enumerate(email):
            if string == '+':
                at_index = email.index('@', index)
                normalized_email.append(email[at_index:])
                unique_emails.add(''.join(normalized_email))
                break
            if string == '.':
                continue
            if string == '@':
                normalized_email.append(email[index:])
                unique_emails.add(''.join(normalized_email))
                break
            normalized_email.append(string)

    return len(unique_emails)
