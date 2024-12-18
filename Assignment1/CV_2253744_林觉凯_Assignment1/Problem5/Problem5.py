import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 使用SIFT检测关键点并计算描述符
def detectKeypointsAndDescriptors(img):
    # 先将图像转换为灰度
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 调库使用SIFT算法检测关键点和计算描述符
    sift = cv2.SIFT_create()

    # 检测关键点并计算描述符，detectAndCompute 函数中自带 DoG
    keypoints, descriptors = sift.detectAndCompute(gray, None)

    return keypoints, descriptors

# 使用FLANN匹配器进行关键点匹配，并应用Lowe's Ratio Test筛选出好的匹配点
def matchKeypoints(des1, des2, kp1, kp2):
    # FLANN 匹配器参数
    FLANN_INDEX_KDTREE = 1
    indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    searchParams = dict(checks=50)  
    
    # 创建 FLANN 匹配器
    flann = cv2.FlannBasedMatcher(indexParams, searchParams)
    
    # 执行 KNN 匹配
    matches = flann.knnMatch(des1, des2, k=2)
    
    # 使用Lowe's Ratio Test筛选匹配点
    goodMatches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            goodMatches.append(m)
    
    return goodMatches

# 使用匹配的关键点对两幅图像进行拼接
def stitchImages(img1, img2, kp1, kp2, goodMatches):
    # 提取匹配点的坐标
    points1 = np.float32([kp1[m.queryIdx].pt for m in goodMatches]).reshape(-1, 1, 2)
    points2 = np.float32([kp2[m.trainIdx].pt for m in goodMatches]).reshape(-1, 1, 2)

    # 检查匹配点数量是否足够
    if len(points1) < 4 or len(points2) < 4:
        raise ValueError("Not enough good matches after filtering.")

    # 调库使用RANSAC算法计算单应矩阵
    H, mask = cv2.findHomography(points1, points2, cv2.RANSAC, 5.0)

    h, w, _ = img2.shape
    # 将第一张图像变换到第二张图像的视角
    panorama = cv2.warpPerspective(img1, H, (w*2, h))
    panorama[0:h, 0:w] = img2

    return panorama

# 使用SIFT和FLANN匹配器从两幅图像创建全景图
def createPanorama(imagePath1, imagePath2):
    img1 = cv2.imread(imagePath1)
    img2 = cv2.imread(imagePath2)

    # 检测两幅图像中的关键点和描述符
    kp1, des1 = detectKeypointsAndDescriptors(img1)
    kp2, des2 = detectKeypointsAndDescriptors(img2)

     # 匹配两幅图像之间的关键点
    goodMatches = matchKeypoints(des1, des2, kp1, kp2)

    # 使用匹配的关键点拼接图像
    panorama = stitchImages(img1, img2, kp1, kp2, goodMatches)

    return img1, img2, kp1, kp2, goodMatches, panorama

# 使用matplotlib显示图像，并且将图像保存到指定路径
def displayImage(image, title="Image", savePath=None):
    plt.figure(figsize=(10, 5))
    plt.title(title)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.tight_layout()

    if savePath:
        cv2.imwrite(savePath, image)
    plt.show()

# 绘制并显示图像中未经Lowe's Ratio Test筛选的关键点
def drawKeypoints(image, keypoints, title, keypointSize=15, keypointThickness=3, savePath=None):
    # 使用 cv2.drawKeypoints 进行关键点绘制
    imgWithKp = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    for kp in keypoints:
        center = tuple(map(int, kp.pt))
        radius = int(kp.size / 2)  
        
        # 一些参数的设置
        color = np.random.randint(0, 255, size=3).tolist()
        cv2.circle(imgWithKp, center, radius, color, keypointThickness)
    
    displayImage(imgWithKp, title, savePath)

# 绘制并显示图像中经过Lowe's Ratio Test筛选的关键点
def drawFilteredKeypoints(img, keypoints, goodMatches, title, keypointSize=15, keypointThickness=3, savePath=None):
    # 根据goodMatches筛选出过滤后的关键点，并检查索引是否越界
    filteredKeypoints = []
    for m in goodMatches:
        if m.queryIdx < len(keypoints):  
            filteredKeypoints.append(keypoints[m.queryIdx])

    # 使用 cv2.drawKeypoints 绘制过滤后的关键点
    imgWithKp = cv2.drawKeypoints(img, filteredKeypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    for kp in filteredKeypoints:
        center = tuple(map(int, kp.pt))
        radius = int(kp.size / 2)  

        # 一些参数的设置
        color = np.random.randint(0, 255, size=3).tolist()
        cv2.circle(imgWithKp, center, radius, color, keypointThickness)

    displayImage(imgWithKp, title, savePath)

# 绘制两幅图像之间的匹配点
def drawMatches(img1, img2, kp1, kp2, goodMatches, lineThickness=6, savePath=None):
    # 创建一张空白图像用于显示匹配结果
    imgMatches = cv2.drawMatches(img1, kp1, img2, kp2, goodMatches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]

    # 画出匹配线条
    for match in goodMatches:
        # 获取匹配的关键点
        pt1 = np.int32(kp1[match.queryIdx].pt)
        pt2 = np.int32(kp2[match.trainIdx].pt)

        # 一些参数的设置
        color = np.random.randint(0, 255, size=3).tolist()
        cv2.line(imgMatches, pt1, (pt2[0] + w1, pt2[1]), color, lineThickness)
 
    displayImage(imgMatches, "Keypoint Matches", savePath)

# 输入图片的路径
imgPath1 = "image/input/right.png" 
imgPath2 = "image/input/left.png"  

# 通过拼接两幅图像生成全景图
img1, img2, kp1, kp2, goodMatches, panorama = createPanorama(imgPath1, imgPath2)

os.makedirs('image', exist_ok=True)

# 保存并显示左图和右图中未经Lowe's Ratio Test筛选的的关键点
drawKeypoints(img1, kp1, "Keypoints in Right Image before Lowe's Ratio Test", keypointSize=40, keypointThickness=6, savePath='image/output/originKeypointsRight.png')
drawKeypoints(img2, kp2, "Keypoints in Left Image before Lowe's Ratio Test", keypointSize=40, keypointThickness=6, savePath='image/output/originKeypointsLeft.png')

# 保存并显示左图和右图中经过Lowe's Ratio Test筛选的的关键点
drawFilteredKeypoints(img1, kp1, goodMatches, "Keypoints in Right Image after Lowe's Ratio Test", keypointSize=40, keypointThickness=6, savePath='image/output/filteredKeypointsRight.png')
drawFilteredKeypoints(img2, kp2, goodMatches, "Keypoints in Left Image after Lowe's Ratio Test", keypointSize=40, keypointThickness=6, savePath='image/output/filteredKeypointsLeft.png')

# 保存并显示左图和右图之间的关键点匹配
drawMatches(img1, img2, kp1, kp2, goodMatches, lineThickness=5, savePath='image/output/keypointMatches.png')

# 保存并显示拼接结果的全景图
displayImage(panorama, "Panorama", savePath='image/output/panoramaResult.png')
