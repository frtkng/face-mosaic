import cv2

def apply_mosaic(img, x, y, w, h, mosaic_scale=0.05):
    face = img[y:y+h, x:x+w]
    small = cv2.resize(face, (max(1, int(w * mosaic_scale)), max(1, int(h * mosaic_scale))), interpolation=cv2.INTER_LINEAR)
    mosaic_face = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
    img[y:y+h, x:x+w] = mosaic_face
    return img

def mosaic_faces(image_path, output_path="mosaic_output.jpg", max_faces=10):
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        print("画像が読み込めませんでした。パスを確認してください。")
        return
    image_rgb = image.copy()
    
    # Load Haar cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
    faces = sorted(faces, key=lambda rect: rect[2]*rect[3], reverse=True)[:max_faces]

    # Apply mosaic to faces
    for (x, y, w, h) in faces:
        image_rgb = apply_mosaic(image_rgb, x, y, w, h)

    # Save result
    cv2.imwrite(output_path, image_rgb)
    print(f"保存しました: {output_path}")

# 使用例
if __name__ == "__main__":
    mosaic_faces("PXL_20250501_080038842.jpg", "mosaic_PXL_20250501_080038842.jpg")

