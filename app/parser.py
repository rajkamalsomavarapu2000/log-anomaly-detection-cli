import re
from typing import Optional, Tuple

LOG_RE = re.compile(
    r"^(?P<ts>\\S+)\\s+(?P<level>[A-Z]+)\\s+(?P<msg>.*)$"
)

def parse_line(line: str) -> Tuple[Optional[str], Optional[str], str]:
    m = LOG_RE.match(line.strip())
    if not m:
        return None, None, line.strip()
    return m.group("ts"), m.group("level"), m.group("msg")

def fingerprint(level: Optional[str], msg: str) -> str:
    s = re.sub(r"\\b\\d+\\b", "<NUM>", msg)
    s = re.sub(r"\\s+", " ", s).strip()
    return f"{level or 'UNK'} | {s}"
