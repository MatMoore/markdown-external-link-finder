from markdown_external_link_finder import url_is_absolute


def test_relative_scheme():
    assert url_is_absolute('//foo.com')


def test_relative_url():
    assert not url_is_absolute('/foo')


def test_local_relative_url():
    assert not url_is_absolute('./foo')


def test_url_is_considered_relative_if_no_scheme():
    assert not url_is_absolute('www.foo.com')


def test_absolute_url():
    assert url_is_absolute('https://www.foo.com')


def test_absolute_url_with_path():
    assert url_is_absolute('https://www.foo.com/foo')


def test_filename():
    assert not url_is_absolute('foo')
