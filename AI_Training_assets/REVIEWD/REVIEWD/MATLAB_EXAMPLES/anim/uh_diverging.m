function cm = uh_diverging(n)
%UH_DIVERGING  uhslate (negative) - white (zero) - uhred (positive).
%   Both ends carry comparable lightness (slate L* ~37, uhred L* ~45). An
%   earlier version used uhred blended 50% toward white, which put a dark grey
%   against a pale pink: negatives read as heavy black streaks and positives
%   were invisible, so the whole table looked like noise on white.
%
%   The route markers reuse uhred at full saturation. They stay readable on top
%   of the texture because they are solid full-width bars with a leader arrow,
%   not isolated pixels.
if nargin < 1, n = 256; end
C  = uh_palette();
lo = C.slate;
hi = C.red;
t  = linspace(0,1,n).';
cm = [interp1([0 .5 1],[lo(1) 1 hi(1)],t), ...
      interp1([0 .5 1],[lo(2) 1 hi(2)],t), ...
      interp1([0 .5 1],[lo(3) 1 hi(3)],t)];
end
