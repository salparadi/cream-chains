# Overview
CREAMchains is a simple module used to organize EVM chain data like routers, factories and aggregators. Much of this work has been inspired by [BowTiedDevil](https://twitter.com/BowTiedDevil). Go check out his stack [Degen Code](https://www.degencode.com/) for great insight into blockchain work with Python and Vyper. TY Devil!

Other CREAM modules are forthcoming which leverage this data.

## Prerequisites
Python version 3.10 or newer.

## Dependencies
Just a few, which should auto-install if you don't already have them:

- eth_typing ([pypi](https://pypi.org/project/eth-typing/))
- eth_utils ([pypi](https://pypi.org/project/eth-utils/))
- ujson ([pypi](https://pypi.org/project/ujson/))

## Installation
At the moment the only way to install is from source. Use `git clone` to create a local copy of this repo, then install with `pip install -e /path/to/repo`. This creates an editable installation that can be imported into a script or Python REPL using `import cream_chains`.

# How the hell do I use this?
This is just a helper that provides some base info about various chains for use in other CREAM tooling. Import it with `import cream_chains` or `from cream_chains import chain_data`