import numpy as np
import matplotlib.pyplot as plt

# 设置图片字体
plt.rcParams['font.sans-serif'] = ['Times New Roman', 'SimHei']  

# 题目所给的数据点
dataPoints = [
    (-2, 0), (0, 0.9), (2, 2.0), (3, 6.5), (4, 2.9), (5, 8.8), 
    (6, 3.95), (8, 5.03), (10, 5.97), (12, 7.1), (13, 1.2), 
    (14, 8.2), (16, 8.5), (18, 10.1)
]

# 计算通过两个点的直线的斜率和截距
def calculateSlopeIntercept(point1, point2):
    # 若直线垂直于x轴，斜率无穷大，截距为x坐标
    if point2[0] - point1[0] == 0:  
        return np.inf, point1[0]  
    
    # 计算直线的斜率和截距
    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
    intercept = point1[1] - slope * point1[0]
    return slope, intercept

# 利用最后获得的内点集合，使用最小二乘法拟合直线
def leastSquaresFit(inliers):
    x_coords = np.array([point[0] for point in inliers])
    y_coords = np.array([point[1] for point in inliers])
    
    # 最小二乘法拟合
    A = np.vstack([x_coords, np.ones(len(x_coords))]).T
    slope, intercept = np.linalg.lstsq(A, y_coords, rcond=None)[0]
    
    return slope, intercept

# 使用RANSAC算法从数据点集中拟合直线
def ransacFitLine(dataPoints, maxIterations=100, distanceThreshold=1.0):
    bestInliers = []  # 存储最佳内点集合
    bestSlope, bestIntercept = 0, 0  # 存储最佳的斜率和截距
    numPoints = len(dataPoints)  # 数据点数量

    # 进行多次迭代以找到最佳拟合直线
    # 迭代次数可改，这里默认迭代次数为100，但是本题3次以上结果基本上稳定了
    for _ in range(maxIterations):
        # 随机选择两个点
        randomIdx1, randomIdx2 = np.random.choice(numPoints, 2, replace=False)
        point1, point2 = dataPoints[randomIdx1], dataPoints[randomIdx2]

        # 通过这两个点计算直线的斜率和截距
        slope, intercept = calculateSlopeIntercept(point1, point2)

        currentInliers = []
        for point in dataPoints:
            # 计算点到直线的垂直距离
            distance = abs(point[1] - (slope * point[0] + intercept)) / (np.sqrt(1 + slope**2) if slope != np.inf else 1)
            
            # 如果距离小于我们一开始设定的阈值，则认为该点为内点
            if distance < distanceThreshold:
                currentInliers.append(point)

        # 如果当前模型的内点数多于之前的最佳模型，更新最佳模型
        if len(currentInliers) > len(bestInliers):
            bestInliers = currentInliers

    # 使用最小二乘法拟合最佳内点集合，得到最终的直线斜率和截距
    # 注意这里老师上课也特意讲过是要用这些全部内点拟合，并不是选的那两个点
    if bestInliers:
        bestSlope, bestIntercept = leastSquaresFit(bestInliers)

    # 返回最佳拟合直线的斜率、截距和内点集合
    return bestSlope, bestIntercept, bestInliers

# 使用RANSAC算法拟合直线
bestSlope, bestIntercept, bestInliers = ransacFitLine(dataPoints)

xValues = np.linspace(-3, 20, 400)
yValues = bestSlope * xValues + bestIntercept if bestSlope != np.inf else [bestIntercept] * len(xValues)
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# 显示原始的所有数据点集
axes[0].scatter(*zip(*dataPoints), color='gray', label='Before')
axes[0].set_title('Before')
axes[0].grid(True)

# 显示经过RANSAC算法拟合后的直线
axes[1].scatter(*zip(*dataPoints), color='gray', label='All Data Points', marker='o')
axes[1].scatter(*zip(*bestInliers), color='red', label='Inliers', marker='o')
outliers = [point for point in dataPoints if point not in bestInliers]
axes[1].scatter(*zip(*outliers), color='black', label='Outliers', marker='x')
axes[1].plot(xValues, yValues, color='blue', label=f'Fitted Line: y = {bestSlope:.3f}x + {bestIntercept:.3f}')
axes[1].set_title('RANSAC Fitted Line and Inliers')
axes[1].legend(loc='upper left', fontsize='small')
axes[1].grid(True)

plt.tight_layout()
# 保存图片
fig.savefig('image/Problem4.png')  

plt.show()
