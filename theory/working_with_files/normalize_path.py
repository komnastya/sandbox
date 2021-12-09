def normalize(path: str) -> str:
    """Simplifies path by removing unnecessary fragments from it."""
    parts = path.split('/')
    new_parts = []
    for part in parts:
        if part == '..':
            new_parts.pop()
        elif part == '' or part == '.':
            continue
        else:
            new_parts.append(part)
    return '/' + '/'.join(new_parts)
