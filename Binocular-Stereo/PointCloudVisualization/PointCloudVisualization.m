% read stereoParams
stereoParams = load('stereoParams.mat');
stereoParams = stereoParams.stereoParams;

% visualize extrinsics
showExtrinsics(stereoParams);

% select a pair of stereo images, calculate its disparity map and point cloud
path = '.\stereo-imgs\';
leftImg = imread('D:\2024_2025\ComputerVision\Binocular-Stereo\PointCloudVisualization\test-left\test-left.jpg');
rightImg = imread('D:\2024_2025\ComputerVision\Binocular-Stereo\PointCloudVisualization\test-right\test-right.jpg');

% rectify stereo images based on stereoParams
% reprojectionMatrix
[frameLeftRect, frameRightRect, reprojectionMatrix] = rectifyStereoImages(leftImg, rightImg, stereoParams);

frameLeftGray  = im2gray(frameLeftRect);
frameRightGray = im2gray(frameRightRect);

frameLeftGray = imguidedfilter(frameLeftGray, 'DegreeOfSmoothing', 0.05);
frameRightGray = imguidedfilter(frameRightGray, 'DegreeOfSmoothing', 0.05);

% calculate disparity map
disparityMap = disparitySGM(frameLeftGray, frameRightGray, 'DisparityRange', [0 128], 'UniquenessThreshold', 10);

% create disparity map display window and add mouse move callback
fig = figure('Name', 'Disparity Map with Depth');
h = imshow(disparityMap, [0, 128]);
title('Disparity Map - Move mouse to see depth');
colormap jet
colorbar

% create depth value text display
depthText = text(10, 30, 'Depth: -- m', ...
                'Color', 'red', ...
                'FontSize', 14, ...
                'BackgroundColor', [1 1 1 0.7], ...
                'Parent', gca);

% add mouse move callback
set(fig, 'WindowButtonMotionFcn', @(src,event)mouseMoveCallback(src,event,disparityMap,stereoParams,depthText));

% calculate 3D point cloud based on disparity map and reprojectionMatrix
points3D = reconstructScene(disparityMap, reprojectionMatrix);

% filter invalid points
validPoints = points3D(:, :, 3) < 10; % assume points with z-coordinate greater than 10 meters are invalid
points3D(validPoints) = NaN;

% convert physical units from millimeters to meters
points3D = points3D ./ 1000;
ptCloud = pointCloud(points3D, 'Color', frameLeftRect);

% store point cloud to local disk
pcwrite(ptCloud,'result.ply','Encoding','ascii');

% create a point cloud viewer
player3D = pcplayer([-3, 3], [-3, 3], [0, 3], 'VerticalAxis', 'y', ...
    'VerticalAxisDir', 'down');

% view the generated 3D point cloud
view(player3D, ptCloud);

% mouse move callback function
function mouseMoveCallback(src, ~, disparityMap, stereoParams, depthText)
    try
        % get mouse position
        pos = get(gca, 'CurrentPoint');
        x = round(pos(1,1));
        y = round(pos(1,2));
        
        % check if mouse is within image range
        if x >= 1 && x <= size(disparityMap,2) && y >= 1 && y <= size(disparityMap,1)
            % get local disparity value
            windowSize = 5;
            yRange = max(1, y-floor(windowSize/2)):min(size(disparityMap,1), y+floor(windowSize/2));
            xRange = max(1, x-floor(windowSize/2)):min(size(disparityMap,2), x+floor(windowSize/2));
            localDisparities = disparityMap(yRange, xRange);
            
            % calculate weighted average of valid disparities
            validDisparities = localDisparities(localDisparities > 0);
            
            if ~isempty(validDisparities)
                % calculate disparity using weighted average
                weights = exp(-(validDisparities - median(validDisparities)).^2 / (2 * std(validDisparities)^2));
                disparity = sum(validDisparities .* weights) / sum(weights);
                
                % calculate depth value
                baseline = abs(stereoParams.TranslationOfCamera2(1)); % baseline length (mm)
                focalLength = mean(stereoParams.CameraParameters1.FocalLength); % use average focal length
                depth = (baseline * focalLength) / (disparity * 1000); % convert to meters
                
                % limit depth range
                depth = min(max(depth, 0.1), 10);
                
                % update depth value display
                set(depthText, 'String', sprintf('Depth: %.3f m', depth));
                set(depthText, 'Position', [x+10, y, 0]);
            else
                set(depthText, 'String', 'Invalid depth');
            end
        end
    catch e
        fprintf('Error in mouse callback: %s\n', e.message);
    end
end