#include <iostream>
#include <opencv2/opencv.hpp>
#include <random>  
using namespace std;

int main()
{
    // ��ȡͼ���ҽ�׳�Լ��
    cv::Mat imgl = cv::imread("left.png");
    cv::Mat imgr = cv::imread("right.png");
    if (!imgl.data || !imgr.data)
    {
        cout << "Reading Images Failure!" << endl;
        return -1;
    }

    // ��ͼ��ת��Ϊ�Ҷ�ͼ��
    cv::Mat grayImgL, grayImgR;
    cv::cvtColor(imgl, grayImgL, cv::COLOR_BGR2GRAY);
    cv::cvtColor(imgr, grayImgR, cv::COLOR_BGR2GRAY);

    // ֱ��ͼ���⻯
    cv::equalizeHist(grayImgL, grayImgL);
    cv::equalizeHist(grayImgR, grayImgR);

    // ����ORB�����
    auto orbDetector = cv::ORB::create();
    // ����ͼ��Ĺؼ���
    vector<cv::KeyPoint> kpsl, kpsr;  
    // �ؼ���������
    cv::Mat dcpsl, dcpsr;  

    // ��Ⲣ����ؼ����������
    orbDetector->detectAndCompute(grayImgL, cv::Mat(), kpsl, dcpsl);
    orbDetector->detectAndCompute(grayImgR, cv::Mat(), kpsr, dcpsr);

    // ʹ�ñ���ƥ��������ƥ��
    cv::Ptr<cv::DescriptorMatcher> matcher = cv::DescriptorMatcher::create(cv::DescriptorMatcher::BRUTEFORCE);
    std::vector<cv::DMatch> matchers;
    matcher->match(dcpsl, dcpsr, matchers);

    // ����ƥ��������ֵ��ƥ�����С�ڸ�ֵ�ĵ����Ϊ����Чƥ��
    float matchThreshold = 320.0;

    // ����������־���飬���ڱ���Ƿ���ƥ���
    std::vector<bool> matchedL(kpsl.size(), false);
    std::vector<bool> matchedR(kpsr.size(), false);

    // ����ͼ��ƴ��
    cv::Mat imgMatches = imgl.clone();
    cv::hconcat(imgl, imgr, imgMatches);  

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> colorDist(0, 255);

    // ����ƥ������
    for (const auto& match : matchers)
    {
        if (match.distance < matchThreshold)  // ֻ����ƥ�����С����ֵ�ĵ�
        {
            matchedL[match.queryIdx] = true;  // ��ͼ��Ĺؼ��㱻ƥ��
            matchedR[match.trainIdx] = true;  // ��ͼ��Ĺؼ��㱻ƥ��

            cv::Scalar randomColor(colorDist(gen), colorDist(gen), colorDist(gen));
            cv::line(imgMatches, kpsl[match.queryIdx].pt, kpsr[match.trainIdx].pt + cv::Point2f(imgl.cols, 0), randomColor, 9);
        }
    }

    // ԲȦ��ǹؼ���
    for (size_t i = 0; i < kpsl.size(); ++i)
    {
        // һЩ����������
        cv::Scalar randomColor(colorDist(gen), colorDist(gen), colorDist(gen));
        cv::circle(imgMatches, kpsl[i].pt, 15, randomColor, 6);
    }
    for (size_t i = 0; i < kpsr.size(); ++i)
    {
        // һЩ����������
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
