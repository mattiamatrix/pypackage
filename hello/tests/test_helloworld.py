from hello.helloworld import print_hello_world


def test_print_hello_world():
    """

    :return:
    """

    assert print_hello_world() == "Hello, World!"
