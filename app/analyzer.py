from collections import Counter
from typing import List, Dict

def analyze_patterns(lines: List[str]) -> Dict:
    counts = Counter(lines)
    total = sum(counts.values())

    rare = sorted(counts.items(), key=lambda x: x[1])[:10]

    return {
        "total_lines": total,
        "unique_patterns": len(counts),
        "rare_patterns": rare
    }
