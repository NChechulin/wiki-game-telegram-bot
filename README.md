# Wiki Game telegram bot

## About

This is a telegram bot which automates [Wiki Game](https://en.wikipedia.org/wiki/Wikipedia:Wiki_Game).
You have to send it a link to an article on English Wikipedia and it'll try to find a "path" to Adolf Hitler article _(Adolf Hitler was **not** my personal choice. Some people claim that this article was a part of original Wiki Game rules)_.

Please, note that it may take several minutes and in some cases can not be done.
Also sometimes the text of the link and the title of the article, to which it leads, don't match, so Ctrl+F will not always work out.

![Example](https://habrastorage.org/webt/vr/db/bv/vrdbbv4nz1xlkwfqrse7ll6gtje.png)

## Project structure

```
.
├── bot.py              - Main bot file
├── config.py           - Configuration file
├── core
│   ├── node.py         - Node, which represents an article
│   ├── parsing.py      - Functions for parsing wikipedia page
│   └── search.py       - Logic for searching the correct path
├── README.md           - This file
├── requirements.txt    - Python requirements file
```

## Setup and configuration

1. Clone the repo: `git clone https://github.com/NChechulin/everything-leads-to-hitler.git`
2. Install requirements: `pip install -r requirements.txt`
3. [Register a new bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
4. Insert a token of your bot in `config.json`
5. Create a `cache.db` sqlite3 database. It has to contain table `cache` with 2 text fields: `current` and `next`
6. Run `python3 bot.py` to start the bot. You may also change the messages, which bot sends.
