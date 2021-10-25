# Dice Roller for Discord

```
/roll 2d3+5
```

Then replied:

```
(1+3)+5 = 9
```

## Installation

[Click here to add the bot in your server](https://discord.com/api/oauth2/authorize?client_id=901999374744301628&permissions=277025392640&scope=bot)

## Cheatsheet

See [xdice Documentation](https://xdice.readthedocs.io/en/latest/dice_notation.html) for more.

Here are some examples from the documentation:

- `1d6` - Roll a 6-sided die
- `1d6+3` - Roll a 6-sided die, then add 3
- `2*(1d6+3)` - Roll a 6-sided die, add 3, then multiply by 2
- `3d6L2` - Roll three 6-sided dice, and drop the two lowest.
- `R2(1d6+3)` - Similar to `1d6+3+1d6+3`
- `1d%` - Similar to `1d100`
- `d6` - Similar to `1d6`
- `min(1d6+10,3d6)` - Keep the minimal score between `1d6+10` and `3d6`

## Development

```sh
git clone https://github.com/fj68/discord-bot-roller.git
cd discord-bot-roller
# Assuming you have Python 3.10.0 (if not, use pyenv: pyenv install 3.10.0 && pyenv local 3.10.0)
python3 -m venv .venv
python3 -m pip install -r requirements.txt
# Now you go!
```

## License

MIT
