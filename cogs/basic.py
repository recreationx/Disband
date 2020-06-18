import discord
from discord.ext import commands
import random


class Basic(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online.")

    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        if member == None:
            ctx.send("Member argument missing.")
        else:
            show_avatar = discord.Embed(
                title=f"{member}",
                description=f"[**Avatar URL**]({member.avatar_url})",
                color=discord.Color.darker_grey(),
            )
            show_avatar.set_image(url=f"{member.avatar_url}")
            await ctx.send(embed=show_avatar)

    @commands.command(aliases=["8ball", "eightball"])
    async def _8ball(self, ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
        ]
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


def setup(client):
    client.add_cog(Basic(client))
