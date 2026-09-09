import pytest


def test_create_user():
    user = User("James", "testpassword")
    assert user.name == "James"
    assert user.password == "testpassword"


def test_validate_user_details():
    with pytest.raises(ValueError):
        user = User("", "")


def test_user_persisted():
    user1 = User("Agnes", "testpass")
    user2 = User("Frans", "testpass")
    assert len(User.all) == 2
    assert user1 in User.all


def test_change_password():
    user = User("Agnes", "testpass")
    user.password = "testpass2"
    assert user.password == "testpass2"
    with pytest.raises(ValueError):
        user.password = ""


def test_validate_user():
    user = User("Agnes", "testpass")
    assert User.validate_user(user.name, user.password) == True
    with pytest.raises(Exception):
        User.validate_user("", "")
