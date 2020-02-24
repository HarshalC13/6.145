def approx_integral(f, lo, hi, num_regions):
    h = float(hi - lo) / num_regions
    s = 0.0
    s += f(lo) / 2.0
    for i in range(1, num_regions):
        s += f(lo + i * h)
    s += f(hi) / 2.0
    return s * h
