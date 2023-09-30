def format_uptime(seconds: int) -> str:
    d = seconds // (3600 * 24)
    h = seconds // 3600 % 24
    m = seconds % 3600 // 60
    s = seconds % 3600 % 60
    if d > 0:
        return "{:02d}D {:02d}H {:02d}m {:02d}s".format(d, h, m, s)
    elif h > 0:
        return "{:02d}H {:02d}m {:02d}s".format(h, m, s)
    elif m > 0:
        return "{:02d}m {:02d}s".format(m, s)
    elif s > 0:
        return "{:02d}s".format(s)
    return "-"
