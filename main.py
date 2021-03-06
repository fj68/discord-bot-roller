from discord import Intents
from discord.ext.commands import Bot
import os
import traceback
import argparse
import xdice

APP = 'ROLLER'

class Dice:
    def __init__(self, pattern):
        self.pattern = pattern
        self.compiled = xdice.compile(pattern)
        self.rolled = None
    def roll(self):
        self.rolled = self.compiled.roll()
        return self
    def __str__(self):
        if self.rolled is None:
            self.roll()
        fstr = self.compiled.format_string
        scores = [f"({'+'.join(str(d) for d in score.detail)})" for score in self.rolled.scores()]
        return f"{fstr.format(*scores)} = {str(self.rolled)}"

def main(token=None, name=None, prefix=None):
    TOKEN = token or os.getenv(f"{APP}_TOKEN")
    COMMAND_NAME = name or os.getenv(f"{APP}_COMMAND_NAME", default='roll')

    if TOKEN is None:
        raise RuntimeError('Token for Discord Bot API is not provided.')
    
    bot = Bot(command_prefix="/", intents=Intents.default())
    
    @bot.event
    async def on_command_error(ctx, error):
        original = getattr(error, "original", error)
        msg = ''.join(traceback.TracebackException.from_exception(original).format())
        await ctx.send(msg)
    
    @bot.command(name=COMMAND_NAME)
    async def roll_command(ctx, *args):
        pattern = ' '.join(args)
        if pattern:
            await ctx.reply(str(Dice(pattern)), mention_author=False)
    
    bot.run(TOKEN)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Dice Roller - Discord Bot',
        epilog='These options will override values set by env vars.'
    )
    parser.add_argument('--token', metavar=f"TOKEN",
                        help="Discord Bot API Token [{API}_TOKEN]")
    parser.add_argument('--name', metavar="NAME",
                        help="Command Name (default: 'roll') [{API}_COMMAND_NAME]")
    args = parser.parse_args()
    main(**vars(args))
