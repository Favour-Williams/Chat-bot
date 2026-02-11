def run_python_file(working_directory, file_path, args=None):
    import subprocess
    import os

    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Security check: Ensure file is inside the permitted directory
        common = os.path.commonpath([working_dir_abs, target_file_abs])
        if common != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(target_file_abs):
            return f'Error: The file "{file_path}" does not exist within the working directory'

        if not os.path.isfile(target_file_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        if not target_file_abs.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        # Build the command to run the Python file
        cmd = ["python", target_file_abs]
        if args:
            cmd.extend(args)

        # Run the command and capture output
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            cwd=working_dir_abs, 
            timeout=30
        )

        output_parts = []

        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        stdout_text = result.stdout.strip() if result.stdout else ""
        stderr_text = result.stderr.strip() if result.stderr else ""

        if not stdout_text and not stderr_text:
            output_parts.append("No output produced")
        else:
            if stdout_text:
                output_parts.append(f"STDOUT:\n{stdout_text}")
            if stderr_text:
                output_parts.append(f"STDERR:\n{stderr_text}")

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: {str(e)}"