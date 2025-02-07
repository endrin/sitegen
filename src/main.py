import os
import shutil


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
    mirror("static", "public", verbose=True)


if __name__ == "__main__":
    main()
