function C = uh_palette()
%UH_PALETTE  Deck colours for the embedding-route animation.
%   Hexes taken verbatim from beamercolorthemeUHTraining.sty, via the
%   epic-infographics `uh-training` design language.
%
%   uhteal #00B388 is deliberately ABSENT: it measures 2.69:1 on white,
%   below the 3:1 contrast floor for a data mark. uhgreen carries the result.
C.red   = [200  16  46]/255;   % uhred    - token path
C.ocher = [185 120   0]/255;   % uhocher  - position path
C.green = [  0 134 108]/255;   % uhgreen  - the result, h^(0)
C.slate = [ 84  88  90]/255;   % uhslate  - structure, axes, rules
C.gray  = [136 139 141]/255;   % uhgray   - inactive
C.bg    = [  1   1   1];       % white ground, matches the slide
C.ink   = [  0   0   0];
end
