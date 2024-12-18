% import stereoParams
stereoParams = load('stereoParams.mat');
stereoParams = stereoParams.stereoParams;

% visualize extrinsics
showExtrinsics(stereoParams);

% define image path
leftImagePath = 'D:\2024_2025\ComputerVision\Binocular-Stereo\MultiView3DReconstruction\CreatePlys\left\';
rightImagePath = 'D:\2024_2025\ComputerVision\Binocular-Stereo\MultiView3DReconstruction\CreatePlys\right\';

% define output path for ply files
plyOutputPath = 'D:\2024_2025\ComputerVision\Binocular-Stereo\MultiView3DReconstruction\CreatePlys\plys\';

% loop through 1 to 24 image pairs
for i = 1:24
    % build image file name
    leftImgFile = fullfile(leftImagePath, sprintf('left_%d.jpg', i));
    rightImgFile = fullfile(rightImagePath, sprintf('right_%d.jpg', i));

    % read images
    leftImg = imread(leftImgFile);
    rightImg = imread(rightImgFile);

    % rectify images based on stereoParams
    [frameLeftRect, frameRightRect, reprojectionMatrix] = rectifyStereoImages(leftImg, rightImg, stereoParams);

    % convert to grayscale
    frameLeftGray  = im2gray(frameLeftRect);
    frameRightGray = im2gray(frameRightRect);

    % apply guided filter
    frameLeftGray = imguidedfilter(frameLeftGray, 'DegreeOfSmoothing', 0.05);
    frameRightGray = imguidedfilter(frameRightGray, 'DegreeOfSmoothing', 0.05);

    % calculate disparity map
    disparityMap = disparitySGM(frameLeftGray, frameRightGray, 'DisparityRange', [0 128], 'UniquenessThreshold', 10);

    % calculate 3D points based on disparity map and reprojectionMatrix
    points3D = reconstructScene(disparityMap, reprojectionMatrix);

    % filter invalid points
    validPoints = points3D(:, :, 3) < 10; % assume z coordinate greater than 10 meters is invalid
    points3D(validPoints) = NaN;

    % convert physical unit from millimeters to meters
    points3D = points3D ./ 1000;
    
    % create point cloud object
    ptCloud = pointCloud(points3D, 'Color', frameLeftRect);

    % save point cloud to local disk
    plyFileName = fullfile(plyOutputPath, sprintf('result_%d.ply', i));
    pcwrite(ptCloud, plyFileName, 'Encoding', 'ascii');

    % print progress information
    fprintf('Processed pair %d and saved as %s\n', i, plyFileName);
end

% note: in actual operation, you may need to adjust the code according to actual conditions, such as checking if the image exists.
