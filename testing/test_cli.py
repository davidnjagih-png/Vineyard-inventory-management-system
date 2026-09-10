import subprocess
import os


def run_cli_command(command):
    """Helper to CLI command and capture output"""
    return subprocess.run(command, capture_output=True, text=True)


# user cli tasks
def test_login_user():
    """test addin user from cli"""
    result = run_cli_command(
        ["python", "-m", "lib.cli_tool", "login", "Alice", "testpass"]
    )

    print("STDERR:", result.stderr)

    assert "Welcome back Alice" in result.stdout


def test_add_user():
    """test addin user from cli"""
    result = run_cli_command(
        ["python", "-m", "lib.cli_tool", "add_user", "Alice", "testpass"]
    )

    print("STDERR:", result.stderr)

    assert "User Alice added to users" in result.stdout


def test_add_user_when_unauthenticated_fails():
    """test addin user from cli"""
    logout = run_cli_command(["python", "-m", "lib.cli_tool", "logout"])

    assert "Logged out" in logout.stdout

    result = run_cli_command(
        ["python", "-m", "lib.cli_tool", "add_user", "Alice", "testpass"]
    )

    print("STDERR:", result.stderr)

    assert (
        "Sorry, You can not access this information without an Admin account."
        in result.stdout
    )


# wine inventory
