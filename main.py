import os

PARTS = [
    "My agent promised a zero-downtime deployment, ",
    "and delivered: the site ",
    "was already down when it started.",
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
