def solution(data, ext, val_ext, sort_by):

    col_idx = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3,
    }
    
    ext_idx = col_idx[ext]
    sort_idx = col_idx[sort_by]
    

    filtered = [row for row in data if row[ext_idx] < val_ext]
    

    filtered.sort(key=lambda row: row[sort_idx])
    
    return filtered
