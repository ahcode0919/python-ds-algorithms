from strings.unique_emails import unique_email_addresses


def test_unique_email_addresses():
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com",
        "testemail@leetcode.com"
    ]
    assert unique_email_addresses(emails) == 2
