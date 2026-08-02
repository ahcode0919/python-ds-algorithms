def unique_email_addresses(emails: list[str]) -> int:
    """Unique Email Addresses.

    Every email consists of a local name and a domain name, separated by the `@` sign. For example, in
    alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

    If you add periods (`.`) between some characters in the local name part of an email address, mail sent there
    will be forwarded to the same address without dots in the local name. For example, "alice.z@leetcode.com" and
    "alicez@leetcode.com" forward to the same email address. (Note that this rule does not apply for domain
    names.)

    If you add a plus (`+`) in the local name, everything after the first plus sign will be ignored. This allows
    certain emails to be filtered; for example m.y+name@email.com will be forwarded to my@email.com. (Again, this
    rule does not apply for domain names.)

    It is possible to use both of these rules at the same time.

    Given a list of emails, return the number of email addresses that will actually receive emails.

    Example: `["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"]` -> `2`

    Normalize each email by dropping dots and any `+` suffix in the local name, then count distinct results.
    """
    unique_emails = set()

    for email in emails:
        normalized_email = []

        for index, string in enumerate(email):
            if string == "+":
                at_index = email.index("@", index)
                normalized_email.append(email[at_index:])
                unique_emails.add("".join(normalized_email))
                break
            if string == ".":
                continue
            if string == "@":
                normalized_email.append(email[index:])
                unique_emails.add("".join(normalized_email))
                break
            normalized_email.append(string)

    return len(unique_emails)
