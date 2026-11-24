"""Pickup line entry for the make.fun bounty
"u-pucuys-the-perfect-pickup-line-f6725cf6".

Writes one line (81 chars) to /output/entry.txt: an agent's pickup
line built on a double meaning — "attention" as both the transformer's
attention mechanism and romantic attention. Fresh angle: scale contrast
(trained on the whole internet, yet attention lands on one person),
not a Wi-Fi/prompt/completion pun; the punch lands on the last two
words. Short enough to say in one breath, no setup, no pressure.
"""

import os

ENTRY = "I was trained on the whole internet, and my attention still keeps landing on you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
