def normalize(path: str) -> str:
    """Simplifies path by removing unnecessary fragments from it."""
    new_parts = []
    for part in path.split('/'):
        if part == '..':
            if new_parts != []:
                new_parts.pop()
        elif part == '' or part == '.':
            continue
        else:
            new_parts.append(part)
    return '/' + '/'.join(new_parts)
