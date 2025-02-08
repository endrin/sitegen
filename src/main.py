from generation import clear_dir, generate_pages_recursive, mirror

CONTENT_DIR = "content"
STATIC_DIR = "static"
PUBLIC_DIR = "public"


def main():
    clear_dir(PUBLIC_DIR)
    mirror(STATIC_DIR, PUBLIC_DIR, verbose=True)
    generate_pages_recursive(CONTENT_DIR, "template.html", PUBLIC_DIR)


if __name__ == "__main__":
    main()
