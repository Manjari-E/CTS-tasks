import shutil

copied = set()

try:
    source = "sample.txt"
    destination = "backup/sample.txt"

    if source not in copied:
        shutil.copy(source, destination)
        copied.add(source)

    with open("backup.log", "a") as log:
        log.write("Backup completed\n")

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")