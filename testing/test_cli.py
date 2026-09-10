import subprocess
import os


def run_cli_command(command):
    """Helper to CLI command and capture output"""
    return subprocess.run(command, capture_output=True, text=True)


def tes_loggin_user():
    result = run_cli_command(["python", "-m", "main", "login", "Alice", "testpass"])
    assert f"username: Alicv"


def test_add_user():
    """test addin user from cli"""
    result = run_cli_command(
        ["python", "-m", "lib.cli_tool", "add_user", "Alice", "testpass"]
    )

    print("STDERR:", result.stderr)

    assert f"User Alice added to users" in result.stdout
