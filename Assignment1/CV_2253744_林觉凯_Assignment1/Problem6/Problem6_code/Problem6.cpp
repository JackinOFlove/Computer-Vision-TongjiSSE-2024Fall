#include <iostream>
#include <opencv2/opencv.hpp>
#include <random>  
using namespace std;

int main()
{
    // 读取图像并且健壮性检查
    cv::Mat imgl = cv::imread("left.png");
    cv::Mat imgr = cv::imread("right.png");
    if (!imgl.data || !imgr.data)
    {
        cout << "Reading Images Failure!" << endl;
        return -1;
    }

    // 将图像转化为灰度图像
    cv::Mat grayImgL, grayImgR;
    cv::cvtColor(imgl, grayImgL, cv::COLOR_BGR2GRAY);
    cv::cvtColor(imgr, grayImgR, cv::COLOR_BGR2GRAY);

    // 直方图均衡化
    cv::equalizeHist(grayImgL, grayImgL);
    cv::equalizeHist(grayImgR, grayImgR);

    // 创建ORB检测器
    auto orbDetector = cv::ORB::create();
    // 左右图像的关键点
    vector<cv::KeyPoint> kpsl, kpsr;  
    // 关键点描述符
    cv::Mat dcpsl, dcpsr;  

    // 检测并计算关键点和描述符
    orbDetector->detectAndCompute(grayImgL, cv::Mat(), kpsl, dcpsl);
    orbDetector->detectAndCompute(grayImgR, cv::Mat(), kpsr, dcpsr);

    // 使用暴力匹配器进行匹配
    cv::Ptr<cv::DescriptorMatcher> matcher = cv::DescriptorMatcher::create(cv::DescriptorMatcher::BRUTEFORCE);
    std::vector<cv::DMatch> matchers;
    matcher->match(dcpsl, dcpsr, matchers);

    // 设置匹配距离的阈值，匹配距离小于该值的点才认为是有效匹配
    float matchThreshold = 320.0;

    // 创建布尔标志数组，用于标记是否有匹配点
    std::vector<bool> matchedL(kpsl.size(), false);
    std::vector<bool> matchedR(kpsr.size(), false);

    // 进行图像拼接
    cv::Mat imgMatches = imgl.clone();
    cv::hconcat(imgl, imgr, imgMatches);  

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> colorDist(0, 255);

    // 绘制匹配线条
    for (const auto& match : matchers)
    {
        if (match.distance < matchThreshold)  // 只处理匹配距离小于阈值的点
        {
            matchedL[match.queryIdx] = true;  // 左图像的关键点被匹配
            matchedR[match.trainIdx] = true;  // 右图像的关键点被匹配

            cv::Scalar randomColor(colorDist(gen), colorDist(gen), colorDist(gen));
            cv::line(imgMatches, kpsl[match.queryIdx].pt, kpsr[match.trainIdx].pt + cv::Point2f(imgl.cols, 0), randomColor, 9);
        }
    }

    // 圆圈标记关键点
    for (size_t i = 0; i < kpsl.size(); ++i)
    {
        // 一些参数的设置
        cv::Scalar randomColor(colorDist(gen), colorDist(gen), colorDist(gen));
        cv::circle(imgMatches, kpsl[i].pt, 15, randomColor, 6);
    }
    for (size_t i = 0; i < kpsr.size(); ++i)
    {
        // 一些参数的设置
        cv::Scalar randomColor(colorDist(gen), colorDist(gen), colorDist(gen));
        cv::circle(imgMatches, kpsr[i].pt + cv::Point2f(imgl.cols, 0), 15, randomColor, 6);
    }

    cv::namedWindow("Match", cv::WINDOW_NORMAL);
    cv::resizeWindow("Match", 1300, 500);  
    imshow("Match", imgMatches);
    cv::imwrite("Match.png", imgMatches);
    cv::waitKey(0);  

    return 0;
}
