import os


def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # 2. Security check: Ensure file is inside the permitted directory
        common = os.path.commonpath([working_dir_abs, target_file_abs])
        if common != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file_abs):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Ensure the parent directory exists
        parent_dir = os.path.dirname(target_file_abs)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)

        with open(target_file_abs, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{target_file_abs}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {str(e)}"