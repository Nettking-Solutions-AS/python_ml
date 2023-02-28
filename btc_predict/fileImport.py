def fileImport(file_name):
    """
    Reads the contents of the specified file and returns them as a string.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The contents of the file as a string.
    """
    try:
        # Open the file and read its contents
        with open(file_name, "r") as f:
            file_content = f.read()

        # Return the contents of the file
        return file_content
    except:
        print('No local cache.')
        return None