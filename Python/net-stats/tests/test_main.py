from unittest.mock import MagicMock, patch

from myproject.main import get_public_ip, speed_test


def test_get_public_ip():
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"ip": "1.2.3.4"}
    with patch("myproject.main.requests.get", return_value=mock_resp):
        assert get_public_ip() == "1.2.3.4"


def test_speed_test():
    mock_test = MagicMock()
    mock_test.download.return_value = 100.23 * 10**6
    mock_test.upload.return_value = 50.12 * 10**6
    mock_test.results.ping = 25.07

    with patch("myproject.main.st.Speedtest", return_value=mock_test):
        assert speed_test() == (100.23, 50.12, 25.07)
