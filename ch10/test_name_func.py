from name_func import get_formatted_name


def test_first_last_name():
    formatted_name = get_formatted_name("da", "heige")
    print(f"formatted_name:{formatted_name}")
    assert formatted_name == "Da Heige"


def test_first_name():
    formatted_name = get_formatted_name("da", "heige")
    if formatted_name.find("Da") > -1:
        print("first name equal")
    else:
        print("test success")
    assert "Da" in formatted_name
