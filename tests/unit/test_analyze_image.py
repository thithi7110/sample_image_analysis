import os
from dotenv import load_dotenv
load_dotenv()
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
    assert response.success == expected_response["success"]
    assert response.message == expected_response["message"]
    assert response.estimated_data == expected_response["estimated_data"]

def test_example_com_with_requests_mock():
    image_path = "/path/to/image.jpg"
    expected_response = {
        "success": True,
        "message": "success",
        "estimated_data": {"class": 3, "confidence": 0.8683}
    }

    with requests_mock.Mocker() as m:
        m.post("http://example.com/", json=expected_response)
        analyze_image = AnalyzeImage()
        analyze_image.use_mock_api = False  # 実際のAPIを使用する設定
        response = analyze_image.analyze(image_path)
        print(response)
        print(expected_response)
        assert response.success == expected_response["success"]
        assert response.message == expected_response["message"]
        assert response.estimated_data == expected_response["estimated_data"]
        
def test_error_api_call(analyze_image):
    os.environ['EXAPMLE_API_STATUS'] = '{"is_mock":"true","is_mock_error":"true"}'
    image_path = "/path/to/image.jpg"
    expected_response = {
        "success": False,
        "message": "Error:E50012",
        "estimated_data": {}
    }

    analyze_image = AnalyzeImage()
    analyze_image.use_mock_api = False  # 実際のAPIを使用する設定
    response = analyze_image.analyze(image_path)
    assert response.success == expected_response["success"]
    assert response.message == expected_response["message"]
    assert response.estimated_data == expected_response["estimated_data"]