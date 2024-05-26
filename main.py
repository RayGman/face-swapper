import config
import insightface
from insightface.app import FaceAnalysis

config.AppFaceAnalysis = FaceAnalysis(name='buffalo_l')
config.AppFaceAnalysis.prepare(ctx_id=0, det_size=(640, 640))
config.Swaper = insightface.model_zoo.get_model('inswapper_128.onnx', download=False, download_zip=False)