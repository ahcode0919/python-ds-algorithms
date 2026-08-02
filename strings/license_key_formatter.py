"""License Key Formatter.

Given a license string which consists only of alphanumeric characters and dashes, the string is separated into
`N+1` groups by `N` dashes.

Given a `group_length`, reformat the string so that each group contains exactly that many characters, except for
the first group, which may be shorter but must still contain at least one character. There must be a dash
inserted between groups, and all lowercase letters should be converted to uppercase.

Example: `"5F3Z-2e-9-w"`, `group_length = 3` -> `"5F-3Z2-E9W"`
"""


def license_key_formatter(license_str: str, group_length: int) -> str:
    """Strip existing dashes, uppercase the string, then re-chunk it into dash-separated groups."""
    license_keys = license_str.replace("-", "").upper()
    remainder = len(license_keys) % group_length

    start = 0
    end = remainder if remainder > 0 else group_length
    license_groups = []

    while end <= len(license_keys):
        license_groups.append(license_keys[start:end])
        start = end
        end += group_length

    return "-".join(license_groups)
