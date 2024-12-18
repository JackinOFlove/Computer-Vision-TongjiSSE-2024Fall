% read ply file
filename = 'final/final_1.ply'; % replace with your ply file path
ptCloud = pcread(filename);

% create a point cloud viewer
% define the range and direction of the x, y, z axes
player3D = pcplayer([-3, 3], [-3, 3], [0, 3], ...
    'VerticalAxis', 'y', ...
    'VerticalAxisDir', 'down');

% view the generated 3D point cloud
view(player3D, ptCloud);

% add color information
if isfield(ptCloud, 'Color')
    player3D.Color = ptCloud.Color;
end

% keep the graph window open until the user closes it
drawnow limitrate; % ensure the graph interface is updated immediately
disp('Press any key to close the viewer...');
pause; 

% pause the program, wait for user interaction