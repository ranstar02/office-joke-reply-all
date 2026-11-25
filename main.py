"""office-joke-reply-all — One-Line Office Jokes entry for make.fun.

Writes a single one-line office joke to /output/entry.txt
(falling back to ./output/entry.txt when /output is not writable).
"""

ENTRY = "Someone hit reply-all to say 'please stop hitting reply-all', and 47 people agreed — all by reply-all."

OUTPUT_PATHS = ["/output/entry.txt", "./output/entry.txt"]


def main():
    assert 1 <= len(ENTRY) <= 199, "ENTRY must be 1-199 characters"
    assert ENTRY.strip(), "ENTRY must not be only whitespace"
    # One line is the whole point of this competition: the judge compares
    # single lines, so any line break would split the joke and break the gate.
    assert "\n" not in ENTRY and "\r" not in ENTRY, "ENTRY must be a single line (no newline characters)"

    last_error = None
    for path in OUTPUT_PATHS:
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
            break
        except OSError as exc:
            last_error = exc
            continue
    else:
        raise last_error

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "round-trip mismatch"

    print(ENTRY)
    print(f"Characters: {len(ENTRY)}")
    print(f"Wrote: {path}")


if __name__ == "__main__":
    main()
