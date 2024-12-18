% read point cloud
ptClouds = cell(1, 24); % to store all point clouds
for i = 1:24
    ptClouds{i} = pcread(sprintf('final/final_%d.ply', i)); % read each point cloud
end

% Initial Alignment
% select the first point cloud as the base
basePtCloud = ptClouds{1};

for i = 2:24
    % apply ICP coarse registration to each point cloud
    ptCloudTransformed = ptClouds{i};
    [tform, ptCloudAligned] = pcregistericp(ptCloudTransformed, basePtCloud, 'MaxIterations', 50, 'Tolerance', [0.001, 0.001], 'Metric', 'pointToPoint');
    ptClouds{i} = ptCloudAligned;  % update to the aligned point cloud
end

% Fine Alignment
% on the basis of coarse registration, use more fine ICP refinement
for i = 2:24
    ptCloudTransformed = ptClouds{i};
    [tform, ptCloudAligned] = pcregistericp(ptCloudTransformed, basePtCloud, 'MaxIterations', 100, 'Tolerance', [0.0001, 0.0001], 'Metric', 'pointToPlane');
    ptClouds{i} = ptCloudAligned;
end

% Point Cloud Fusion
% merge all aligned point clouds
mergedPtCloud = ptClouds{1};
for i = 2:24
    mergedPtCloud = pcmerge(mergedPtCloud, ptClouds{i}, 0.01); % 0.01 is the merging distance threshold
end

% Post-Processing
% use voxel filtering to reduce the density of the point cloud
gridSize = 0.005; % set the voxel size
mergedPtCloud = pcdownsample(mergedPtCloud, 'gridAverage', gridSize);

% visualize the merged point cloud
player3D = pcplayer([-3, 3], [-3, 3], [0, 3], 'VerticalAxis', 'y', 'VerticalAxisDir', 'down');
view(player3D, mergedPtCloud);

% save the final point cloud
pcwrite(mergedPtCloud, 'mergedInitial.ply');
