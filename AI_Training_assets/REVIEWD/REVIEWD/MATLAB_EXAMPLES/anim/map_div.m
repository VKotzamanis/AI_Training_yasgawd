function rgb = map_div(A, cm, pct, mlim)
%MAP_DIV  Map a signed array to truecolor on a SYMMETRIC scale about zero.
%   rgb = MAP_DIV(A, cm)              limit = 99th percentile of |A|
%   rgb = MAP_DIV(A, cm, pct)         limit = pct-th percentile of |A|
%   rgb = MAP_DIV(A, cm, pct, mlim)   limit = mlim, given explicitly
%
%   Symmetric limits are not cosmetic: with asymmetric limits zero stops being
%   white and the diverging colormap lies about the sign of the data.
%
%   Pass MLIM to put several arrays on ONE scale. e, p and h0 share a limit so
%   that the real magnitude difference between them stays visible - at layer 0
%   the position row is about 2.6x the token row, and per-array scaling would
%   erase exactly that fact.
%
%   Without MLIM the limit is a ROBUST percentile and values beyond it clip.
%   On wte_img the block-mean pulls most values toward zero while a few outlier
%   tokens are large, so max(|A|) renders the table blank white. Clipping is a
%   display choice; it changes no value, only the colour limit.
if nargin < 3 || isempty(pct), pct = 99; end
if nargin < 4 || isempty(mlim)
    v = sort(abs(A(:)));
    mlim = v(max(1, min(numel(v), round(pct/100*numel(v)))));
end
if mlim == 0, mlim = max(abs(A(:))); end
if mlim == 0, mlim = 1; end
x   = min(max(A/mlim, -1), 1);
idx = round((x(:)+1)/2 * (size(cm,1)-1)) + 1;
rgb = reshape(cm(idx,:), [size(A,1) size(A,2) 3]);
end
