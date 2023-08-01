

def test_version():
    from dmc_apitest import __version__
    assert isinstance(__version__,str)