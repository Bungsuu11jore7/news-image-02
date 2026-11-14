# Field Notes — news-image-01 (entry 2)

One image that sums up the world's news of Friday 13 November 2026,
drawn as a page from a reporter's notebook: six pinned clipping
cards, each with a pictogram, a kicker, a headline and a short
summary — plus a date stamp, ruled paper and tape, so it reads as one
person's record of the day rather than a stock front page.

1. Europe takes its seat at the Ukraine peace table: Dublin agrees a
   five-country team for the talks, as Kyiv fires 1,200 drones in one
   of the war's biggest strikes.
2. The US shoots down two Iranian drones bound for Bahrain; Iran
   claims it hit a US radar — that claim is unverified.
3. Nvidia chief Jensen Huang resigns after 33 years; shares fall as
   much as 14%; CFO Colette Kress becomes interim chief.
4. The FAA lifts a nationwide ground stop: departures resume after a
   communications failure halts every US airport for 4+ hours.
5. Brooklyn collapse: the DA opens a criminal probe; all eight
   victims are named, two of them children; the city will check
   about 100 sites.
6. At COP31 in Antalya the UN chief urges drastic emissions cuts as
   pledged climate finance falls about 70% from 2025.

Every fact was checked against reporting of 13 November 2026 (AP,
Reuters, FAA, Carbon Brief). Where a claim is unverified, the image
says so.

## How it differs from entry 1

Entry 1 ("The World in One Day", 94.14%) was a newspaper front page
with a 5x7 bitmap font. This entry is a different image: a notebook
page with anti-aliased type that stays legible at 300 pixels across,
two new stories (the FAA ground stop and COP31) in place of the
Microsoft outage and the Binance seizure, fresh 13-November angles on
the shared stories (the Brooklyn criminal probe, the Dublin talks
agreement), and a corrected Nvidia figure — shares fell as much as
14%, not 16%.

## Run

    python3 main.py

Writes `entry.png` (1024x1024, PNG, 129,786 bytes). The program only
copies the shipped image with the Python standard library, no network,
no randomness — two runs write byte-identical files.
