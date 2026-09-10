import pytest

from lib.users import User

@pytest.fixture(autouse=True)
def reset_users():
    User.all.clear()


def test_create_user():
    """test user can be created"""
    user = User("James", "testpassword")
    assert user.name == "James"
    assert user.password == "testpassword"


def test_validate_user_details():
    """test to validate user details"""
    with pytest.raises(ValueError):
        User("", "")


def test_user_persisted():
    """test user is persisted in class parameter all"""
    user1 = User("Agnes", "testpass")
    user2 = User("Frans", "testpass")
    assert len(User.all) == 2
    assert user1 in User.all


def test_change_password():
    """test user can change password and id validated for empty strings"""
    user = User("Agnes", "testpass")
    user.password = "testpass2"
    assert user.password == "testpass2"
    with pytest.raises(ValueError):
        user.password = ""


def test_validate_user():
    """test user validation return validated user"""
    user = User("Agnes", "testpass")
    assert User.validate_user(user.name, user.password) == user #changed from true to return actual object
    with pytest.raises(Exception):
        User.validate_user("", "")
