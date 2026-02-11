import os
# from config import MAX_CHARS
def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # 2. Security check: Ensure file is inside the permitted directory
        common = os.path.commonpath([working_dir_abs, target_file_abs])
        if common != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(target_file_abs):
            return f'Error: The file "{file_path}" does not exist within the working directory'

        if not os.path.isfile(target_file_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
    
        MAX_CHARS = 10000

        with open(target_file_abs, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                file_content_string += f'[...File "{target_file_abs}" truncated at {MAX_CHARS} characters]'
            
        return file_content_string
    except Exception as e:
        return f"Error: {str(e)}"