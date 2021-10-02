from service.geobase import Geobase


def test_init():
    Geobase()


def test_validate():
    Geobase(validate=True)


def test_linter():
    Geobase(linter=True)
