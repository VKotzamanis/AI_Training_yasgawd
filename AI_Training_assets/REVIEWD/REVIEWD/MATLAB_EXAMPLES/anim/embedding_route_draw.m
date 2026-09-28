function embedding_route_draw(S, t)
%EMBEDDING_ROUTE_DRAW  One frame of the token -> hidden-state route.
%   S  struct from gpt2_slice.mat     t  seconds, 0 .. 7.5
%
%   Every value drawn is real GPT-2 small. Units are figure-normalised (0..1),
%   y up, one axes for the whole frame.
%
%   NUMBERS. Six of 768 dimensions are printed. The selection rule is fixed in
%   the extractor and stated on screen: the six with the largest |h0|. Their
%   real indices (301, 357, 529, 671, 675, 680) are drawn as column headers and
%   tick-marked at their true positions along the 768-wide strip, so nobody can
%   mistake them for "the first six".
%
%   ROUNDING. round(e) + round(p) ~= round(e+p) for about 40% of dimensions at
%   any fixed precision. One of the six columns shows this. The caption says so
%   rather than the display hiding it: no value printed here has been adjusted.
%
%   DISPLAY CHOICES, deliberate, stated so they can be overruled:
%     wte is drawn in full - 50257 rows block-MEAN-reduced to 700 display rows,
%     and row 7771 lands 15.5% down, so the marker travel is honest.
%     wpe is a MAGNIFIED INSET of its first 48 rows, faded out at the bottom,
%     true count labelled below. At full scale slot 5 of 1024 sits 0.5% down
%     and the marker would not visibly move at all.

C  = uh_palette();
cm = uh_diverging(256);
FT = 'Times New Roman';
FM = get(0,'FixedWidthFontName');

% One colour limit for e, p and h0 so their real magnitudes stay comparable.
pool   = sort(abs([S.e_row(:); S.p_row(:); S.h0_row(:)]));
mStrip = pool(round(0.95*numel(pool)));

% ---- beats: [start duration] seconds ---------------------------------------
B = struct('chip',[0.00 0.45],'tok',[0.45 0.60],'wteM',[1.05 1.35], ...
           'e',[2.40 0.80],'p',[3.20 1.20],'h0',[4.40 1.00],'emph',[5.40 0.70]);

% ---- geometry ---------------------------------------------------------------
G.sentY = 0.945;
G.wte   = [0.175 0.500 0.125 0.320];        % [x ybottom w h]
G.wpe   = [0.175 0.150 0.125 0.190];
G.sX    = [0.415 0.845];                     % strip span
G.eY = 0.845; G.pY = 0.755; G.ruleY = 0.712; G.hY = 0.645;
G.sH = 0.042; G.h0H = 0.055;
G.tX = [0.470 0.855];                        % number-table span
G.thY = 0.445; G.teY = 0.378; G.tpY = 0.308; G.trY = 0.271; G.thhY = 0.207;
WPE_SHOW = 48;

cla; hold on
set(gca,'XLim',[0 1],'YLim',[0 1],'Position',[0 0 1 1],'YDir','normal');
axis off; set(gcf,'Color',C.bg);
% Full-canvas ground patch: without it the rendered bounding box tracks the
% drawn content and the frame size changes as elements appear mid-animation.
patch([0 1 1 0],[0 0 1 1], C.bg, 'EdgeColor','none');

toks = strsplit(S.token_strs,'|');
k    = S.active;  tid = S.token_ids(k);
dims = S.disp_dims(:).';
nD   = numel(dims);

% ============================ STATIC SCENE ===================================
nT = numel(toks); cx = 0.055; w = zeros(1,nT); chipX = zeros(1,nT);
for i = 1:nT, w(i) = 0.016 + 0.0135*numel(strtrim(toks{i})); end
for i = 1:nT
    chipX(i) = cx;
    rectangle('Position',[cx G.sentY-0.026 w(i) 0.052],'Curvature',0.25, ...
              'EdgeColor',C.gray,'LineWidth',1.0);
    text(cx+w(i)/2, G.sentY, strtrim(toks{i}),'FontName',FT,'FontSize',18, ...
         'Color',C.slate,'HorizontalAlignment','center','VerticalAlignment','middle');
    cx = cx + w(i) + 0.014;
end

drawmap(map_div(S.wte_img,cm,97), G.wte); boxline(G.wte, C.slate);
axlab(G.wte,'0','50257',C.slate,FT);
tablabel(G.wte,'wte','word token embedding',C,FT);

wpeIn = S.wpe_img(1:WPE_SHOW,:);
rgbP  = map_div(wpeIn,cm,97);
fade  = ones(WPE_SHOW,1); nf = round(WPE_SHOW*0.30);
fade(end-nf+1:end) = linspace(1,0,nf);
rgbP  = rgbP.*fade + 1.*(1-fade);
drawmap(rgbP, G.wpe); boxline(G.wpe, C.slate);
text(G.wpe(1)-0.012, G.wpe(2)+G.wpe(4),'0','FontName',FT,'FontSize',13, ...
     'Color',C.slate,'HorizontalAlignment','right','VerticalAlignment','middle');
text(G.wpe(1)-0.012, G.wpe(2)-0.020,'1024','FontName',FT,'FontSize',13, ...
     'Color',C.slate,'HorizontalAlignment','right','VerticalAlignment','middle');
tablabel(G.wpe,'wpe','word position embedding',C,FT);

for yy = [G.eY G.pY], slot(G.sX,yy,G.sH,C.gray); end
slot(G.sX,G.hY,G.h0H,C.gray);
text(G.sX(2), G.hY-G.h0H/2-0.030,'768','FontName',FT,'FontSize',13, ...
     'Color',C.slate,'HorizontalAlignment','right');

% dimension callout: ticks at the TRUE positions of the six printed dims
for i = 1:nD
    xt = G.sX(1) + diff(G.sX)*(dims(i)-0.5)/S.d_model;
    line([xt xt],[G.hY-G.h0H/2-0.004 G.hY-G.h0H/2-0.018],'Color',C.slate,'LineWidth',1.0);
    line([xt colx(G.tX,i,nD)],[G.hY-G.h0H/2-0.018 G.thY+0.022], ...
         'Color',C.gray,'LineWidth',0.6);
    text(colx(G.tX,i,nD), G.thY, sprintf('%d',dims(i)),'FontName',FT,'FontSize',15, ...
         'Color',C.slate,'HorizontalAlignment','center','VerticalAlignment','middle');
end
text(G.tX(1)-0.030, G.thY,'dim','FontName',FT,'FontSize',15,'Color',C.gray, ...
     'HorizontalAlignment','right','VerticalAlignment','middle');

% ============================ ANIMATED ROUTE =================================
a = ss(t,B.chip);
if a > 0
    fc = C.red*a + [1 1 1]*(1-a);
    rectangle('Position',[chipX(k) G.sentY-0.026 w(k) 0.052],'Curvature',0.25, ...
              'FaceColor',fc,'EdgeColor',fc);
    text(chipX(k)+w(k)/2, G.sentY, strtrim(toks{k}),'FontName',FT,'FontSize',18, ...
         'Color',[1 1 1]*a + C.slate*(1-a),'HorizontalAlignment','center', ...
         'VerticalAlignment','middle','FontWeight','bold');
end

a = ss(t,B.tok);
if a > 0
    text(0.050, 0.800, ['''' toks{k} ''''],'FontName',FT,'FontSize',21, ...
         'Color',C.slate,'HorizontalAlignment','left');
    text(0.050, 0.727, sprintf('%d',tid),'FontName',FT,'FontSize',42, ...
         'Color',C.red,'HorizontalAlignment','left','FontWeight','bold');
end

% --- wte scan: the marker walks and the six numbers under it change ---------
a = ss(t,B.wteM);
rowFrac = tid / S.n_vocab;
yRow    = G.wte(2)+G.wte(4) - rowFrac*G.wte(4);
if a > 0
    aT  = min(a/0.30,1); yID = 0.735;
    line([0.145 0.145+(G.wte(1)-0.145)*aT],[yID yID],'Color',C.red,'LineWidth',2.2);
    if a > 0.30
        aM = ss01((a-0.30)/0.70);
        yM = (G.wte(2)+G.wte(4)) + (yRow-(G.wte(2)+G.wte(4)))*aM;
        line([G.wte(1) G.wte(1)],[yID yM],'Color',C.red,'LineWidth',2.2);
        marker(G.wte,yM,C.red);
        j = max(1,min(size(S.scan_wte,1), round(aM*size(S.scan_wte,1))));
        text(G.wte(1)+G.wte(3)/2, G.wte(2)-0.030, sprintf('%d',S.scan_wte_ids(j)), ...
             'FontName',FT,'FontSize',15,'Color',C.red, ...
             'HorizontalAlignment','center','VerticalAlignment','middle');
        numrow(0.070, 0.405, G.wte(2)-0.060, S.scan_wte(j,:), C.slate, FM, 13);
    end
end

% --- strip e ----------------------------------------------------------------
a = ss(t,B.e);
if a > 0
    line([G.wte(1)+G.wte(3) G.sX(1)],[yRow G.eY],'Color',C.red,'LineWidth',1.5);
    fillstrip(S.e_row,cm,G.sX,G.eY,G.sH,a,C.red,mStrip);
    text(G.sX(1)-0.016,G.eY,'e','FontName',FT,'FontSize',23,'FontAngle','italic', ...
         'Color',C.red,'HorizontalAlignment','right','VerticalAlignment','middle');
    if a > 0.5
        numrow(G.tX(1),G.tX(2),G.teY,S.e_disp,C.red,FM,17,ss01((a-0.5)/0.5));
        text(G.tX(1)-0.030,G.teY,'e','FontName',FT,'FontSize',20,'FontAngle','italic', ...
             'Color',C.red,'HorizontalAlignment','right','VerticalAlignment','middle');
    end
end

% --- wpe scan and strip p ---------------------------------------------------
a  = ss(t,B.p);
yP = G.wpe(2)+G.wpe(4) - (k-1)/WPE_SHOW*G.wpe(4);
if a > 0
    text(0.050,0.300,sprintf('%d',k-1),'FontName',FT,'FontSize',42, ...
         'Color',C.ocher,'HorizontalAlignment','left','FontWeight','bold');
    aT = min(a/0.25,1);
    line([0.100 0.100+(G.wpe(1)-0.100)*aT],[0.300 0.300],'Color',C.ocher,'LineWidth',2.2);
    if a > 0.22
        aM = ss01((a-0.22)/0.45);
        yM = (G.wpe(2)+G.wpe(4)) + (yP-(G.wpe(2)+G.wpe(4)))*aM;
        line([G.wpe(1) G.wpe(1)],[0.300 yM],'Color',C.ocher,'LineWidth',2.2);
        marker(G.wpe,yM,C.ocher);
        j = max(1,min(size(S.scan_wpe,1), 1+round(aM*(k-1))));
        text(G.wpe(1)+G.wpe(3)/2, G.wpe(2)-0.028, sprintf('%d',j-1), ...
             'FontName',FT,'FontSize',15,'Color',C.ocher, ...
             'HorizontalAlignment','center','VerticalAlignment','middle');
        numrow(0.070, 0.405, G.wpe(2)-0.058, S.scan_wpe(j,:), C.slate, FM, 13);
    end
    if a > 0.45
        aS = ss01((a-0.45)/0.55);
        line([G.wpe(1)+G.wpe(3) G.sX(1)],[yP G.pY],'Color',C.ocher,'LineWidth',1.5);
        fillstrip(S.p_row,cm,G.sX,G.pY,G.sH,aS,C.ocher,mStrip);
        text(G.sX(1)-0.016,G.pY,'p','FontName',FT,'FontSize',23,'FontAngle','italic', ...
             'Color',C.ocher,'HorizontalAlignment','right','VerticalAlignment','middle');
        text(0.362,G.pY,'+','FontName',FT,'FontSize',30,'Color',C.ink, ...
             'HorizontalAlignment','center','VerticalAlignment','middle');
        if aS > 0.5
            numrow(G.tX(1),G.tX(2),G.tpY,S.p_disp,C.ocher,FM,17,ss01((aS-0.5)/0.5));
            text(G.tX(1)-0.030,G.tpY,'p','FontName',FT,'FontSize',20,'FontAngle','italic', ...
                 'Color',C.ocher,'HorizontalAlignment','right','VerticalAlignment','middle');
            text(G.tX(1)-0.062,G.tpY,'+','FontName',FT,'FontSize',20,'Color',C.ink, ...
                 'HorizontalAlignment','center','VerticalAlignment','middle');
        end
    end
end

% --- the rule, h0, and the numeric sum --------------------------------------
a = ss(t,B.h0);
if a > 0
    aR = min(a/0.35,1);
    line([G.sX(1)-0.030 G.sX(1)-0.030+(diff(G.sX)+0.030)*aR],[G.ruleY G.ruleY], ...
         'Color',C.ink,'LineWidth',1.5);
    line([G.tX(1)-0.075 G.tX(1)-0.075+(diff(G.tX)+0.075)*aR],[G.trY G.trY], ...
         'Color',C.ink,'LineWidth',1.5);
    if a > 0.35
        aH = ss01((a-0.35)/0.65);
        fillstrip(S.h0_row,cm,G.sX,G.hY,G.h0H,aH,C.green,mStrip);
        text(G.sX(1)-0.016,G.hY,'{\ith}^{(0)}','FontName',FT,'FontSize',25, ...
             'Interpreter','tex','Color',C.green, ...
             'HorizontalAlignment','right','VerticalAlignment','middle');
        if aH > 0.4
            numrow(G.tX(1),G.tX(2),G.thhY,S.h0_disp,C.green,FM,17,ss01((aH-0.4)/0.6));
            text(G.tX(1)-0.030,G.thhY,'{\ith}^{(0)}','FontName',FT,'FontSize',20, ...
                 'Interpreter','tex','Color',C.green, ...
                 'HorizontalAlignment','right','VerticalAlignment','middle');
        end
    end
end

a = ss(t,B.emph);
if a > 0
    line(G.sX,[G.hY-G.h0H/2-0.010 G.hY-G.h0H/2-0.010], ...
         'Color',C.green*a+[1 1 1]*(1-a),'LineWidth',3.2);
    text(G.tX(2), G.thhY-0.055, 'values rounded to 2 dp', ...
         'FontName',FT,'FontSize',13,'Color',C.gray*a+[1 1 1]*(1-a), ...
         'HorizontalAlignment','right');
end
hold off
end

% ================================ helpers ====================================
function u = ss(t,b),  u = ss01((t-b(1))/b(2)); end
function u = ss01(x),  u = min(max(x,0),1); u = u.*u.*(3-2*u); end
function x = colx(tX,i,n), x = tX(1) + (i-0.5)*diff(tX)/n; end

function drawmap(rgb,g), drawimg(rgb,g(1),g(1)+g(3),g(2)+g(4),g(2)); end

function drawimg(rgb,x0,x1,ytop,ybot)
% image() YData gives the CENTRES of the first and last row, not the outer
% edges. With a 1-row strip that degenerates and the image spans a whole data
% unit - which is what made every strip bleed outside its own outline.
n = size(rgb,1); dy = (ytop-ybot)/(2*n); dx = (x1-x0)/(2*size(rgb,2));
image('XData',[x0+dx x1-dx],'YData',[ytop-dy ybot+dy],'CData',rgb);
end

function boxline(g,col), rectangle('Position',g,'EdgeColor',col,'LineWidth',1.1); end

function axlab(g,top,bot,col,FT)
text(g(1)-0.012,g(2)+g(4),top,'FontName',FT,'FontSize',13,'Color',col, ...
     'HorizontalAlignment','right','VerticalAlignment','middle');
text(g(1)-0.012,g(2),bot,'FontName',FT,'FontSize',13,'Color',col, ...
     'HorizontalAlignment','right','VerticalAlignment','middle');
end

function tablabel(g,name,gloss,C,FT)
text(g(1)+g(3)/2, g(2)+g(4)+0.052, name,'FontName',FT,'FontSize',20, ...
     'Color',C.ink,'HorizontalAlignment','center');
text(g(1)+g(3)/2, g(2)+g(4)+0.022, gloss,'FontName',FT,'FontSize',13, ...
     'FontAngle','italic','Color',C.slate,'HorizontalAlignment','center');
end

function marker(g,y,col)
rectangle('Position',[g(1) y-0.0042 g(3) 0.0084],'FaceColor',col,'EdgeColor',col);
patch(g(1)-[0.013 0.005 0.013], y+[0.009 0 -0.009], col,'EdgeColor','none');
end

function slot(xs,y,h,col)
rectangle('Position',[xs(1) y-h/2 diff(xs) h],'EdgeColor',col,'LineWidth',1.0);
end

function fillstrip(v,cm,xs,y,h,frac,edge,mlim)
n = numel(v); m = max(1,round(frac*n));
rgb = map_div(reshape(v(1:m),1,[]),cm,[],mlim);
rgb = repmat(rgb,[24 1 1]);
drawimg(rgb, xs(1), xs(1)+diff(xs)*m/n, y+h/2, y-h/2);
rectangle('Position',[xs(1) y-h/2 diff(xs) h],'EdgeColor',edge,'LineWidth',1.5);
end

function numrow(x0,x1,y,vals,col,FM,fsz,alpha)
if nargin < 8, alpha = 1; end
c = col*alpha + [1 1 1]*(1-alpha);
n = numel(vals);
for i = 1:n
    text(x0 + (i-0.5)*(x1-x0)/n, y, sprintf('%+.2f',vals(i)), ...
         'FontName',FM,'FontSize',fsz,'Color',c,'Interpreter','none', ...
         'HorizontalAlignment','center','VerticalAlignment','middle');
end
end
