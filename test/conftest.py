import pytest
import tempfile
import os
# 
# @pytest.fixture()
# def cleandir():
#     newpath = tempfile.mkdtemp()
#     os.chdir(newpath)
# 

from pyhamtools.lookuplib import LookupLib

@pytest.fixture(scope="session", params=["a", "", 12.5, -5, {"foo" : "bar"}, [5, "foo"]])
def fixNonUnsignedInteger(request):
    return request.param

@pytest.fixture(scope="session", params=[12.5, -5, 34569, {"foo" : "bar"}, [5, "foo"]])
def fixNonString(request):
    return request.param

@pytest.fixture(scope="session", params=[12.5, -5.5, 34569.0000001])
def fixFloats(request):
    return request.param

@pytest.fixture(scope="session", params=["", "-5.5", "foo bar"])
def fixStrings(request):
    return request.param

@pytest.fixture(scope="session", params=[0, -2322321, 32321321])
def fixIntegers(request):
    return request.param

@pytest.fixture(scope="session", params=[{"foo": "bar"}, {}, {-99.99 : {"foo": 12}}])
def fixDicts(request):
    return request.param

@pytest.fixture(scope="session", params=[["foo", "bar", 99.12], [None, 55, "foo"]])
def fixLists(request):
    return request.param

@pytest.fixture(scope="session", params=[None])
def fixNone(request):
    return request.param



API_KEY = ""
@pytest.fixture(scope="session")
def fixApiKey(request):
    return(API_KEY)

@pytest.fixture(scope="module", params=["clublogapi", "clublogxml", "countryfile"])
def fixGeneralApi(request, fixApiKey):
    """Fixture returning all possible instances of LookupLib"""
    Lib = LookupLib(request.param, fixApiKey)
    # pytest.skip("better later")
    return(Lib)

@pytest.fixture(scope="module")
def fixClublogApi(request, fixApiKey):
    Lib = LookupLib("clublogapi", fixApiKey)
    return(Lib)

@pytest.fixture(scope="module")
def fixClublogXML(request, fixApiKey):
    Lib = LookupLib("clublogxml", fixApiKey)
    return(Lib)

@pytest.fixture(scope="module")
def fixCountryFile(request):
    Lib = LookupLib("countryfile")
    return(Lib)

@pytest.fixture(scope="module")
def fixRedis(request):
    Lib = LookupLib("redis")
    return(Lib)