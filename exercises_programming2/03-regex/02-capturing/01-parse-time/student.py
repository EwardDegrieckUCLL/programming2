import re

def parse_time(string):
    match = re.fullmatch(r'(\d{2}):([0-5][0-9]):([0-5][0-9])([:\.]\d{3})?', string)

    if match:
        h, m, s, ms = match.groups('.000')
        ms = ms[1:]
        return (int(h), int(m), int(s), int(ms))