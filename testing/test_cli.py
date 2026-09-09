import subprocess
import os


def run_cli_command(command):
    """Helper to CLI command and capture output"""
    return subprocess.run(command, capture_output=True, text=True)


def test_add_user():
    """test addin user from cli"""
    result = run_cli_command(
        ["python", "-m", "lib.cli_tool", "add_user", "Alice", "testpass"]
    )

    print("STDERR:", result.stderr)

    assert f"User Alice added to users" in result.stdout


def test_update_password(tmp_path):
    """test uppdate password from cli"""
    script_path = tmp_path / "script.py"
    script_content = f"""
import sys
sys.path.insert(0, '{os.getcwd().replace("\\\\", "/")}')

from lib.users import User

user = User('Alice','testpass')
user.password = 'testpass2'

"""
    script_path.write_text(script_content)

    result = subprocess.run(
        ["python", str(script_path)], capture_output=True, text=True
    )
    assert "Password for User Alice updated." in result.stdout
