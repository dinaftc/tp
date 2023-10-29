def row_to_list(s):
    if '\t' in s:
        return list(s.split())
    else:
        return None
