class CommandExecutionError(Exception):
    def __init__(self, message: str, exit_code: int = None, stdout: str = "", stderr: str = ""):
        super().__init__(message)
        self.message = message
        self.exit_code = exit_code
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self):
        return f"[Exit {self.exit_code}] {self.message}\nSTDOUT: {self.stdout}\nSTDERR: {self.stderr}"
