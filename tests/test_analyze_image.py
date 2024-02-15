import pytest
import requests_mock
from services.analyze_image_service import AnalyzeImage

@pytest.fixture
def analyze_image():
    return AnalyzeImage()


def test_mock_api_call(analyze_image):
    image_path = "/path/to/image.jpg"
    expected_response = {
        "success": True,
        "message": "success",
        "estimated_data": {"class": 3, "confidence": 0.8683}
    }

    # 環境変数をモック状態に設定
    analyze_image.use_mock_api = True

    response = analyze_image.analyze(image_path)
    assert response == expected_response

def test_example_com_with_requests_mock():
    image_path = "/path/to/image.jpg"
    expected_response = {
        "success": True,
        "message": "Analysis Complete",
        "estimated_data": {"class": 1, "confidence": 0.9}
    }

    with requests_mock.Mocker() as m:
        m.post("http://example.com/", json=expected_response)
        analyze_image = AnalyzeImage()
        analyze_image.use_mock_api = False  # 実際のAPIを使用する設定
        response = analyze_image.analyze(image_path)
        assert response == expected_response