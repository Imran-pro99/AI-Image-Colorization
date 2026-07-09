import cv2                                                                                             # type: ignore
import numpy as np                                                                                     # type: ignore
from pathlib import Path

# Folder Paths 
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "Model"
IMAGES_DIR = BASE_DIR / "images"

proto_file = MODEL_DIR / "colorization_deploy_v2.prototxt"
model_file = MODEL_DIR / "colorization_release_v2.caffemodel"
hull_pts = MODEL_DIR / "pts_in_hull.npy"                                                               # cluster center
img_path = IMAGES_DIR / "img2.jpg"

# Check that files exist 
for p in (proto_file, model_file, hull_pts, img_path):
    if not p.exists():
        raise FileNotFoundError(f"Missing file: {p}")

# Load model
net = cv2.dnn.readNetFromCaffe(str(proto_file), str(model_file))
pts = np.load(str(hull_pts))

# Prepare model layers 
class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")
pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

# Read and preprocess image 
img = cv2.imread(str(img_path))
if img is None:
    raise ValueError("Could not read the image. Check imgx.jpg in /images folder.")

scaled = img.astype("float32") / 255.0
lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

# Resize for network
resized = cv2.resize(lab, (224, 224))
L = cv2.split(resized)[0]
L -= 50

# Predict ab channels 
net.setInput(cv2.dnn.blobFromImage(L))
ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
ab = cv2.resize(ab, (img.shape[1], img.shape[0]))

# Merge L with ab and convert to color
L = cv2.split(lab)[0]
colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
colorized = np.clip(colorized, 0, 1)
colorized = (255 * colorized).astype("uint8")

# Display and Save
result = cv2.hconcat([
    cv2.resize(img, (640, 640)),
    cv2.resize(colorized, (640, 640))
])

cv2.imshow("Grayscale → Colorized", result)
cv2.imwrite("output_colorized.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
