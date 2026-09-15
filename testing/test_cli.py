import subprocess
import os


def run_cli_command(command):
    """Helper to CLI command and capture output"""
    return subprocess.run(command, capture_output=True, text=True)


def test_loggin_user():
    result = run_cli_command(["python", "-m", "main", "login", "Alice", "testpass"])
    assert "Logged in as Alice" in result.stdout


def test_loggout_user():
    result = run_cli_command(["python", "-m", "main", "logout"])
    assert "Logged out." in result.stdout


def test_cant_access_protected_if_logout():
    result = run_cli_command(["python", "-m", "main", "logout"])
    assert "You need to be loged in to perform this operation" in result.stdout


# resolver
