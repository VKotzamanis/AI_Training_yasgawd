# Discovery and validation notes

`robots.txt` was fetched first and saved as `00-robots.txt`. Its `User-agent: *` rules disallow action, publishing, sign-in, subscription, inbox, embed, and related paths; none of the archive API, section, or post URLs used here match those disallows.

Discovery endpoint that worked: `https://mikexcohen.substack.com/api/v1/archive?sort=new&limit=50&offset=0`. The endpoint returned JSON post objects and exposed `section_slug`, `section_name`, and `section_id`; posts were filtered strictly on `section_slug == "ml-on-llms"` (section name: `Dissecting LLMs with ML`). Pagination continued by returned-item count until an empty JSON array. The resulting section count is 18. The RSS feed and sitemap were not needed after the complete paginated archive result; this avoids relying on a potentially truncated RSS feed.

Post pages were fetched one at a time with the specified User-Agent and a one-second delay. HTML was converted using `pandoc -f html -t markdown --wrap=none` from the page's `article` element. No post was a paid-only audience, and the page bodies were full-length; the generic site-wide subscription prompt was not treated as a paywall marker. Truncated/paywalled count is 0.

## Self-check

- `jq 'length' 00-index.json` = 18; `ls raw/*.md | wc -l` = 18. Match.
- Rows with HTTP code other than 200: none.
- `raw/*.md` files under 500 bytes: none.
- Opened `raw/drawing-text-heatmaps-to-visualize.md` by eye. It contains the article title, subtitle, and article prose beginning with the “What is a text heatmap?” section, rather than a navigation-only extraction.
