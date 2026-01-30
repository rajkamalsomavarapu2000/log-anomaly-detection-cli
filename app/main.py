import sys
from app.parser import parse_line, fingerprint
from app.analyzer import analyze_patterns

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m app.main <logfile>")
        sys.exit(1)

    path = sys.argv[1]

    with open(path, "r", errors="ignore") as f:
        raw_lines = f.readlines()

    patterns = []
    for line in raw_lines:
        _, level, msg = parse_line(line)
        patterns.append(fingerprint(level, msg))

    result = analyze_patterns(patterns)

    print("Total lines:", result["total_lines"])
    print("Unique patterns:", result["unique_patterns"])
    print("\\nTop rare patterns:")
    for key, count in result["rare_patterns"]:
        print(f"{count:4d}  {key}")

if __name__ == "__main__":
    main()
