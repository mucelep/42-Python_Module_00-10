#!/usr/bin/env python3

def secure_archive(file_name: str, action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name) as file:
                data = file.read()
                return (True, data)
        else:
            with open(file_name, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
    except (FileNotFoundError, PermissionError) as e:
        return (False, str(e))


if __name__ == "__main__":

    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt"))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    content = "askdfjsdklfkhjsdfgksld\nsdhjfhjfsdjhf"
    print(secure_archive("new_file.txt", "w", content))
