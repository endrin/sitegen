import os
import shutil

from generation import generate_page

CONTENT_DIR = "content"
STATIC_DIR = "static"
PUBLIC_DIR = "public"


def mirror(source: str, destination: str, *, verbose=False):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.makedirs(destination, exist_ok=True)

    for entry in os.scandir(source):
        src_path = entry.path
        dst_path = src_path.replace(source, destination)

        if entry.is_dir():
            mirror(src_path, dst_path, verbose=verbose)
            continue

        if verbose:
            print(f"{src_path} -> {dst_path}")
            shutil.copy2(src_path, dst_path)


def main():
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)
    mirror(STATIC_DIR, PUBLIC_DIR, verbose=True)
    generate_page(
        f"{CONTENT_DIR}/index.md", "template.html", f"{PUBLIC_DIR}/index.html"
    )


if __name__ == "__main__":
    main()
