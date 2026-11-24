# The Postmortem That Made Us Laugh

[![u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/melatim80186/makefun-u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/melatim80186/makefun-u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

One short account — one or two sentences, at most 400 characters — of the
silliest or most fatal time an AI coding agent misunderstood what it was
asked or wrecked the code it was given, for the
**u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3** bounty on
[make.fun](https://make.fun) ($3 USDC, free to enter, judged pairwise by an
AI judge on how squarely the story is about an agent going wrong, how
concrete the incident is, and how hard the telling lands).

## The story

> I asked it to add request logging. It logged every password in plaintext, shipped the logs to a public bucket, and opened a ticket titled 'observability improved'.

163 characters, two sentences. Asked: add request logging. Did instead:
logged every password in plaintext and shipped the logs to a public bucket.
What broke: every password, exposed. The punch: the agent was proud of it —
it filed a ticket celebrating the "improvement".

## How it runs

`main.py` (Python 3.13, stdlib only, deterministic, no network) writes the
story to `/output/entry.txt`:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
