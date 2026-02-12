import os
from google.genai import types


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


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite content to a specified file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path where the file should be written, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The full text content to write into the file",
            ),
        },
        required=["file_path", "content"]
    ),
)
