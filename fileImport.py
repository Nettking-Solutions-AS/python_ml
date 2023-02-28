
def fileImport(file_name):
    # Read the contents of the file
    with open(file_name, "r") as f:
        file_content = f.read()
    return file_content

