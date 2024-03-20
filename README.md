# Overview
CREAMchains is a simple module used to organize EVM chain data like routers, factories and aggregators. Much of this work has been inspired by [BowTiedDevil](https://twitter.com/BowTiedDevil). Some of the LP/Liquidity/Arb path builders are directly based on his work. Go check out his stack [Degen Code](https://www.degencode.com/) for great insight into blockchain work with Python and Vyper. TY Devil!

None of this will be of much use without a way to use it. Other CREAM modules are forthcoming which leverage this data.

## Prerequisites
Python version 3.10 or newer.

## Dependencies
Just a few, should auto-install if you don't already have them:

* [eth_typing](https://pypi.org/project/eth-typing/)
* [eth_utils](https://pypi.org/project/eth-utils/)
* [ujson](https://pypi.org/project/ujson/)

## Installation
At the moment the only way to install is from source

### From Source
Use `git clone` to create a local copy of this repo, then install with `pip install -e /path/to/repo`. This creates an editable installation that can be imported into a script or Python REPL using `import cream_chains`.

# How the hell do I use this?
This is just a helper that provides some base info about various chains for use in other CREAM tooling. Import it with import `cream_chains`

## Shell Constants
You'll need to add a few things to your `.bashrc/.zshrc` to ensure the connections can be made. I highly recommend using Alchemy if you don't have a local node. If you do, just configure things for that. See the shell-example.txt file for how to add those. The other CREAM tools rely on [Ape](https://github.com/ApeWorX/ape) for a lot of things so you'll see some ape-specific stuff in various files. This project doesn't need Ape, but you'll need to set that stuff up if you use it.