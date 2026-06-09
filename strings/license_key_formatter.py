

def license_key_formatter(license_str: str, group_length: int) -> str:
    license_keys = license_str.replace('-', '').upper()
    remainder = len(license_keys) % group_length

    start = 0
    end = remainder if remainder > 0 else group_length
    license_groups = []

    while end <= len(license_keys):
        license_groups.append(license_keys[start:end])
        start = end
        end += group_length

    return '-'.join(license_groups)
