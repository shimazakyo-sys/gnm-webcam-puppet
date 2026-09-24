from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(model_asset_path=None)
options = vision.FaceLandmarkerOptions(base_options=base_options)

# FaceLandmarker のデフォルトモデルを取得
model_path = options.base_options.model_asset_path

print("Generated model:", model_path)
