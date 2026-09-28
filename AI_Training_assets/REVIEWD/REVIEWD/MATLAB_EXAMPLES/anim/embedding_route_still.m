%EMBEDDING_ROUTE_STILL  Render the end state of the route as a PNG.
%   This frame is the sign-off artifact AND the last frame of the video, so
%   the two cannot drift apart.
S = load('gpt2_slice.mat');
S.token_strs = char(S.token_strs);
fig = figure('Color','w','Units','pixels','Position',[50 50 1600 900], ...
             'Visible','off','InvertHardcopy','off');
axes('Position',[0 0 1 1]);
embedding_route_draw(S, 7.5);
% print, not exportgraphics: exportgraphics crops to content, which makes the
% output size depend on the frame. PaperPosition pins it to exactly 1920x1080.
set(fig,'PaperUnits','inches','PaperPosition',[0 0 20 11.25],'PaperPositionMode','manual');
print(fig,'embedding_route_still.png','-dpng','-r96');
d = dir('embedding_route_still.png');
fprintf('wrote embedding_route_still.png  %.2f MB\n', d.bytes/1e6);
close all
