import json
import os
from pydantic import BaseModel
from typing import Dict, Any
import requests


class ImageDescriptionResponse(BaseModel):
    success: bool
    message: str
    estimated_data: Dict[str, Any] = {}

class AnalyzeImage:
    def __init__(self):
        # 環境変数の取得:EXAPMLE_API_STATUS
        raw_example_api_status = os.environ.get("EXAPMLE_API_STATUS")
        print("example_api_status:", raw_example_api_status)
        #example_api_statusをjsonに変換
        if(not raw_example_api_status):
            self.is_mock = False
            self.is_mock_error = False
        else:
            example_api_status = json.loads(raw_example_api_status)
            self.is_mock = True if example_api_status.get("is_mock") and example_api_status.get("is_mock").lower() == "true" else False
            self.is_mock_error = True if example_api_status.get("is_mock_error") and example_api_status.get("is_mock_error").lower() == "true" else False

    def analyze(self,image_path) -> ImageDescriptionResponse:
        if self.is_mock:
            # モックAPIの呼び出し
            return self._mock_api_call(image_path)
        else:
            # 実際のAPIの呼び出し
            return self._example_com(image_path)

    # モックAPIの呼び出し(ゆくゆく削除する)
    def _mock_api_call(self,image_path: str) -> ImageDescriptionResponse:
        # モックレスポンスの生成
        if(self.is_mock_error):
            image_description_response = ImageDescriptionResponse(
                success = False,
                message = "Error:E50012",
                estimated_data = {}
            )
        else:
            image_description_response = ImageDescriptionResponse(
                success = True,
                message = "success",
                estimated_data = {
                    "class": 3,
                    "confidence": 0.8683
                }
            )
        return image_description_response
    

    def _example_com(self,image_path: str) -> ImageDescriptionResponse:
        print("example.com start")
        # 実際のAPIエンドポイントURL
        url = "http://example.com/"
        # POSTリクエストの送信
        response = requests.post(url, json={"image_path": image_path})
        # レスポンスのJSONデータを返却
        res_json =  response.json()
        return ImageDescriptionResponse(
            success = res_json["success"],
            message = res_json["message"],
            estimated_data = res_json["estimated_data"]
        )
