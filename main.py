import os

PARTS = [
    "I asked my agent to document the API. ",
    "It documented the API it wished it had built, ",
    "and filed bug reports against reality.",
]


def entry_text():
    return "".join(PARTS)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry_text())


if __name__ == "__main__":
    main()
