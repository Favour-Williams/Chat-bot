import os   
def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        # Will be True or False
        common = os.path.commonpath([working_dir_abs, target_dir])
        valid_target_dir = common == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.exists(target_dir):
            return f'Error: The directory "{directory}" does not exist within the working directory'

        if not os.path.isdir(target_dir):
            return f'Error: The path "{directory}" is not a directory'

        files_info = []
        items = sorted(os.listdir(target_dir))
        for name in items:
            
            full_path = os.path.join(target_dir, name)
            file_size = os.path.getsize(full_path)
            is_dir = os.path.isdir(full_path)
            
            files_info.append(f"- {name}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(files_info)
    except Exception as e:
        return f"Error: {str(e)}"