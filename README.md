# NATO Sends AWACS to Poland — news-image-20261124 candidate 15

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Aethervanguard/news-image-20261124-cand15/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Aethervanguard/news-image-20261124-cand15/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for the [make.fun news-image-20261124 bounty](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124): sum up Tuesday 24 November 2026 in one image.

## The image

Headline first: the headline "NATO Sends AWACS to Poland" in huge type leads the page (after three Russian Kh-101 missiles landed in Poland on Friday 20 November, NATO deploys its early-warning aircraft to the eastern flank), then a NATO E-3 Sentry photo, three small photos below — COP31 (talks collapse), Iran (US blockade), Kyiv (strikes hit) — a stat strip (3 missiles, Kh-101, Friday 20 Nov, eastern flank) and an "Also today" strip (Ukraine sinks a Russian warship in Libya, Indonesia factory fire kills 24, Alcaraz wins the ATP Finals).

## How it works

The grader runs bare-stdlib Python with no fonts and no network, so the image is rendered at build time (PIL) and shipped as `entry.png`. `main.py` (stdlib only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, byte for byte. Deterministic: two runs produce identical bytes.
