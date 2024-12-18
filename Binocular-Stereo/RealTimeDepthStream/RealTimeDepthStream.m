% import stereoParams
stereoParams = load('stereoParams.mat');
stereoParams = stereoParams.stereoParams;

% init camera
leftCam = videoinput('winvideo', 1, 'YUY2_640x480');
rightCam = videoinput('winvideo', 2, 'YUY2_640x480');

% set camera property
set(leftCam, 'FramesPerTrigger', Inf);
set(rightCam, 'FramesPerTrigger', Inf);
set(leftCam, 'ReturnedColorspace', 'rgb');
set(rightCam, 'ReturnedColorspace', 'rgb');

% start camera
start(leftCam);
start(rightCam);

% create real-time video display window
fig = figure('Name', 'Real-Time Stereo Vision', 'NumberTitle', 'off', ...
            'Position', [100, 100, 1200, 800]); % set window size

% create subplot layout
subplot(2, 2, 1); % left top
hLeft = imshow(zeros(480, 640, 3, 'uint8'));
title('Left Camera');

subplot(2, 2, 2); % right top
hRight = imshow(zeros(480, 640, 3, 'uint8'));
title('Right Camera');

subplot(2, 2, [3,4]); % bottom cross
hDisparity = imshow(zeros(480, 640, 'uint8'), [0, 64]);
title('Disparity Map');
colormap(gca, jet);
colorbar;

% create depth value text display
axes_handle = gca;  % get current axis handle
depthText = text(10, 30, 'Depth: -- m', ...
                'Color', 'red', ...
                'FontSize', 14, ...
                'BackgroundColor', [1 1 1 0.7], ...
                'Parent', axes_handle);

% set global variables
global globalDisparityMap globalStereoParams globalAxesHandle globalDepthText;
globalDisparityMap = [];
globalStereoParams = stereoParams;
globalAxesHandle = axes_handle;
globalDepthText = depthText;

% add mouse move callback
set(fig, 'WindowButtonMotionFcn', @mouseMove);

% real-time processing loop
while ishandle(fig)
    try
        % capture left and right camera images
        frameLeft = getsnapshot(leftCam);
        frameRight = getsnapshot(rightCam);
        
        % rectify images
        [frameLeftRect, frameRightRect] = rectifyStereoImages(frameLeft, frameRight, stereoParams);
        
        % convert to grayscale
        frameLeftGray = im2gray(frameLeftRect);
        frameRightGray = im2gray(frameRightRect);
        
        % calculate disparity map
        disparityMap = disparitySGM(frameLeftGray, frameRightGray, ...
                                  'DisparityRange', [0, 64], ...
                                  'UniquenessThreshold', 15);
        
        % update global disparity map
        globalDisparityMap = disparityMap;
        
        % update display
        set(hLeft, 'CData', frameLeftRect);
        set(hRight, 'CData', frameRightRect);
        set(hDisparity, 'CData', disparityMap);
        drawnow limitrate;
        
        % add short delay to reduce CPU usage
        pause(0.01);
        
    catch e
        disp(['Error: ' e.message]);
    end
end

% stop camera
stop(leftCam);
stop(rightCam);
delete(leftCam);
delete(rightCam);
clear leftCam rightCam;

% mouse move callback function
function mouseMove(src, ~)
    global globalDisparityMap globalStereoParams globalAxesHandle globalDepthText;
    
    try
        % get current image axis
        current_axes = get(src, 'CurrentAxes');
        
        % display depth only on disparity map
        if current_axes == globalAxesHandle
            % get current coordinates
            pos = get(current_axes, 'CurrentPoint');
            x = round(pos(1,1));
            y = round(pos(1,2));
            
            % check coordinates are valid
            if ~isempty(globalDisparityMap) && ...
               x >= 1 && x <= size(globalDisparityMap, 2) && ...
               y >= 1 && y <= size(globalDisparityMap, 1)
                
                % get disparity value
                disparity = globalDisparityMap(y, x);
                
                % calculate depth
                if disparity > 0
                    % get baseline and focal length
                    baseline = norm(globalStereoParams.TranslationOfCamera2); % baseline length mm 
                    focalLength = mean([globalStereoParams.CameraParameters1.FocalLength]); % focal length
                    
                    % calculate depth m
                    depth = (baseline * focalLength) / (disparity * 1000);
                    
                    % limit depth range and display
                    depth = min(max(depth, 0.1), 10);
                    
                    % update depth text
                    set(globalDepthText, 'String', sprintf('Depth: %.2f m', depth));
                    set(globalDepthText, 'Position', [x+10, y, 0]);
                    set(globalDepthText, 'Visible', 'on');
                else
                    set(globalDepthText, 'String', 'Invalid depth');
                    set(globalDepthText, 'Position', [x+10, y, 0]);
                    set(globalDepthText, 'Visible', 'on');
                end
            else
                set(globalDepthText, 'Visible', 'off');
            end
        else
            set(globalDepthText, 'Visible', 'off');
        end
    catch e
        disp(['Mouse callback error: ' e.message]);
    end
end