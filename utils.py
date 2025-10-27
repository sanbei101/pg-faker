from typing import List


def set_and_sort(arr: list[str]) -> list[str]:
    arr_set = set(arr)
    # 先按长度排序,长度相同的按字母排序
    arr = sorted(arr_set, key=lambda x: (len(x), x))
    return arr

def format_array_sql(arr: List[str], indent="        "):
    """将 Python 列表格式化为 SQL ARRAY 字面量"""
    arr = list(arr)
    if not arr:
        return "ARRAY[]"
    
    lines = []
    line = indent + "'{}'".format(arr[0])
    for name in arr[1:]:
        if len(line) + len(name) + 4 > 60:
            lines.append(line + ",")
            line = indent + "'{}'".format(name)
        else:
            line += ", '{}'".format(name)
    lines.append(line)
    return "ARRAY[\n" + "\n".join(lines) + "\n    ]"

def format_array_py(arr: List[str],indent="    "):
    """将 Python 列表格式化为 Python 代码中的列表字面量"""
    arr = list(set_and_sort(arr))
    if not arr:
        return "[]"
    
    lines = []
    line = indent + "'{}'".format(arr[0])
    for name in arr[1:]:
        if len(line) + len(name) + 4 > 60:
            lines.append(line + ",")
            line = indent + "'{}'".format(name)
        else:
            line += ", '{}'".format(name)
    lines.append(line)
    return "[\n" + "\n".join(lines) + "\n]"