import pytest

testURL = 'http://192.168.63.59:8702/login'
namePassword = [('sxj', '123456'), ('sxj1', '123456'), pytest.param('sxj', '1234567', marks=pytest.mark.xfail)]
noVerification = [('sxj', '123456')]
