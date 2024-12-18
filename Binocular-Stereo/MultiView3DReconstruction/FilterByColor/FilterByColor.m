% define the input and output folder path
inputFolder = 'ply';  % the folder of the input ply files
outputFolder = 'filter';  % the folder of the output filtered ply files

% ensure the output folder exists
if ~exist(outputFolder, 'dir')
    mkdir(outputFolder);
end

% traverse all the files to be processed from result_1.ply to result_24.ply
for i = 1:24
    inputFile = fullfile(inputFolder, sprintf('result_%d.ply', i));
    outputFile = fullfile(outputFolder, sprintf('filtered_result_%d.ply', i));
    
    % check if the input file exists
    if exist(inputFile, 'file')
        % filter and save the point cloud
        filter_ply_file1(inputFile, outputFile);
    else
        warning(['Input file does not exist: ', inputFile]);
    end
end

disp('Batch filtering completed.');

% define the filtering function
function filter_ply_file1(inputFile, outputFile)
    % read the ply file
    ptCloud = pcread(inputFile);
    
    % get the color information of the point cloud
    colors = ptCloud.Color;
    
    % define the color range
    lowerBound = 170;
    upperBound = 220;
    
    % find the indices of the points whose RGB values are within the specified range
    inRangeIdx = all((colors >= lowerBound) & (colors <= upperBound), 2);
    
    % delete the points whose RGB values are within the specified range
    filteredLocations = ptCloud.Location(~inRangeIdx, :);
    filteredColors = colors(~inRangeIdx, :);
    
    % create a new point cloud object
    filteredPtCloud = pointCloud(filteredLocations, 'Color', filteredColors);
    
    % save the filtered point cloud to a new ply file
    pcwrite(filteredPtCloud, outputFile, 'Encoding', 'ascii');
    
    disp(['Filtered PLY file saved to: ', outputFile]);
end