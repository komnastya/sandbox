from normalize_path import normalize


def test_normalize():
    assert normalize("/") == "/"
    assert normalize("/a/b/c") == "/a/b/c"
    assert normalize("//a//b//c") == "/a/b/c"
    assert normalize("/././a/././b/././c") == "/a/b/c"
    assert normalize("/a/../b") == "/b"
    assert normalize("///././a/..///./b") == "/b"
    assert normalize("/one/two/three/../zero") == "/one/two/zero"
    assert normalize("/.one/.two/..three/../..zero") == "/.one/.two/..zero"
    assert normalize("/..") == "/"
    assert normalize("/a/../..") == "/"
    assert normalize("/a/../../..") == "/"
    assert normalize("/a/../../../b") == "/b"
    assert normalize("/a/./b/../../c") == "/c"
    assert normalize("abc") == "/abc"
