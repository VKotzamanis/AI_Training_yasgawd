%EMBEDDING_ROUTE_ANIM  Render the token -> hidden-state route to MP4 + GIF.
%
%   Frames come from embedding_route_draw, the same function that renders
%   embedding_route_still.png, so the still and the video cannot drift apart.
%   Frames are written with exportgraphics rather than getframe: headless
%   MATLAB (-batch, Visible off) cannot be trusted to capture an off-screen
%   figure, but exportgraphics is deterministic.
%
%   Beats, in seconds (see embedding_route_draw for the table):
%     0.00 chip   0.45 token+ID   1.05 wte marker   2.00 strip e
%     2.70 wpe marker + strip p   3.55 rule + h0    4.40 emphasis
%     5.00 .. 6.00 hold

FPS = 25; T_END = 7.5;
nF  = round(FPS*T_END);
fdir = fullfile(tempdir,'embroute_frames');
if exist(fdir,'dir'), rmdir(fdir,'s'); end
mkdir(fdir);

S = load('gpt2_slice.mat');
S.token_strs = char(S.token_strs);

fig = figure('Color','w','Units','pixels','Position',[50 50 1920 1080], ...
             'Visible','off','InvertHardcopy','off');
ax  = axes('Position',[0 0 1 1]);
set(fig,'PaperUnits','inches','PaperPosition',[0 0 20 11.25],'PaperPositionMode','manual');

fprintf('rendering %d frames ...\n', nF);
tic
for f = 1:nF
    t = (f-1)/FPS;
    embedding_route_draw(S, t);
    print(fig, fullfile(fdir,sprintf('f%04d.png',f)), '-dpng','-r96');
    if mod(f,30)==0, fprintf('  %3d/%d  (%.0fs)\n', f, nF, toc); end
end
close all
fprintf('frames done in %.0f s\n', toc);

% ---- contact sheet: 12 evenly spaced frames, 4 x 3 ------------------------
pick = round(linspace(1,nF,12));
tiles = cell(1,12);
for i = 1:12
    A = imread(fullfile(fdir,sprintf('f%04d.png',pick(i))));
    tiles{i} = imresize(A,[270 480]);
end
sheet = [tiles{1} tiles{2}  tiles{3}  tiles{4}
         tiles{5} tiles{6}  tiles{7}  tiles{8}
         tiles{9} tiles{10} tiles{11} tiles{12}];
imwrite(sheet,'embedding_route_sheet.png');
fprintf('wrote embedding_route_sheet.png (frames %s)\n', mat2str(pick));

fid = fopen('frames_dir.txt','w'); fprintf(fid,'%s',fdir); fclose(fid);
