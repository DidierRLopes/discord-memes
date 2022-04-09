import os
import io
import uuid
import disnake
from disnake.ext import commands
import pyimgur
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from textwrap import wrap
from random import choice
import functools

DISCORD_BOT_API_KEY = os.getenv("DISCORD_BOT_API_KEY")
IMGUR_API_KEY = os.getenv("IMGUR_API_KEY")

bot = commands.Bot(sync_commands_debug=True)
memes_imgur = pyimgur.Imgur(IMGUR_API_KEY)
plt.rcParams["font.family"] = "impact"

def create_and_send_meme():
    def wrapper(func):
        @bot.slash_command(name=func.__name__)
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            embed = disnake.Embed()
            image = plt.imread(f"memes/{kwargs['inter'].data.name}.jpg")
            fig, ax = plt.subplots()
            ax.imshow(image)
            ax.axis('off')

            kwargs["_"] = fig
            fig = func(*args, **kwargs)

            plt.tight_layout()
            img_name = f"{kwargs['inter'].data.name}.jpg"
            imgbytes = io.BytesIO()
            plt.savefig(imgbytes, bbox_inches='tight', transparent=True, pad_inches=0)
            imgbytes.seek(0)
            plt.close("all")
            image = disnake.File(imgbytes, filename=img_name)
            embed.set_image(url=f"attachment://{img_name}")

            await kwargs['inter'].send(embed=embed, file=image)

        return wrapped
    return wrapper


@create_and_send_meme()
def spongebob(inter, text: str = None, _=None):
    if text:
        _.text(
            0.5,
            0.2,
            "\n".join(wrap(''.join(choice((str.upper, str.lower))(c) for c in text), 40)),
            fontsize=20,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def chloe(inter, text: str = None, _=None):
    if text:
        _.text(
            0.5,
            0.2,
            "\n".join(wrap(text.upper(), 40)),
            fontsize=20,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _


@create_and_send_meme()
def dogecheems(inter, dogename: str = None, dogetext: str = None, cheemsname: str = None, cheemstext: str = None, _=None):
    if dogename:
        _.text(
            0.25,
            0.9,
            "\n".join(wrap(dogename.upper(), 20)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if dogetext:
        _.text(
            0.25,
            0.2,
            "\n".join(wrap(dogetext.upper(), 20)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if cheemsname:
        _.text(
            0.75,
            0.8,
            "\n".join(wrap(cheemsname.upper(), 20)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if cheemstext:
        _.text(
            0.75,
            0.2,
            "\n".join(wrap(cheemstext.upper(), 20)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def stonks(inter, text: str = None, _=None):
    if text:
        _.text(
            0.675,
            0.39,
            "\n".join(wrap(text, 15)),
            fontsize=20,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def clown(inter, text1: str = None, text2: str = None, text3: str = None, text4: str = None, _=None):
    if text1:
        _.text(
            0.4,
            0.8,
            "\n".join(wrap(text1.upper(), 25)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text2:
        _.text(
            0.4,
            0.6,
            "\n".join(wrap(text2.upper(), 25)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text3:
        _.text(
            0.4,
            0.4,
            "\n".join(wrap(text2.upper(), 25)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text4:
        _.text(
            0.4,
            0.2,
            "\n".join(wrap(text2.upper(), 25)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _


@create_and_send_meme()
def conspiracy(inter, person: str = None, text: str = None, _=None):
    if person:
        _.text(
            0.5,
            0.8,
            "\n".join(wrap(person.upper(), 60)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text:
        _.text(
            0.5,
            0.2,
            "\n".join(wrap(text.upper(), 60)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def cryingkid(inter, kid: str = None, adult: str = None, text: str = None, _=None):
    if kid:
        _.text(
            0.5,
            0.65,
            "\n".join(wrap(kid.upper(), 35)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if adult:
        _.text(
            0.5,
            0.4,
            "\n".join(wrap(adult.upper(), 35)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text:
        _.text(
            0.5,
            0.18,
            "\n".join(wrap(text.upper(), 35)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def dicaprio(inter, text: str = None, _=None):
    if text:
        _.text(
            0.5,
            0.2,
            "\n".join(wrap(text.upper(), 35)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _


@create_and_send_meme()
def disappointed(inter, text1: str = None, text2: str = None, _=None):
    if text1:
        _.text(
            0.35,
            0.7,
            "\n".join(wrap(text1.upper(), 35)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text2:
        _.text(
            0.35,
            0.3,
            "\n".join(wrap(text2.upper(), 35)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def dosomething(inter, text: str = None, _=None):
    _.text(
        0.55,
        0.7,
        "C'mon, do something",
        fontsize=16,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    if text:
        _.text(
            0.55,
            0.25,
            "\n".join(wrap(text.upper(), 30)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def drake(inter, text1: str = None, text2: str = None, _=None):
    if text1:
        _.text(
            0.7,
            0.7,
            "\n".join(wrap(text1.upper(), 30)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text2:
        _.text(
            0.7,
            0.3,
            "\n".join(wrap(text2.upper(), 30)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def firedog(inter, text: str = None, _=None):
    if text:
        _.text(
            0.33,
            0.7,
            "\n".join(wrap(text.upper(), 35)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def firegirl(inter, text1: str = None, text2: str = None, _=None):
    if text1:
        _.text(
            0.5,
            0.8,
            "\n".join(wrap(text1.upper(), 50)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text2:
        _.text(
            0.5,
            0.2,
            "\n".join(wrap(text2.upper(), 50)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def flextape(inter, person: str = None, problem: str = None, solution: str = None, _=None):
    if person:
        _.text(
            0.42,
            0.6,
            "\n".join(wrap(person.upper(), 30)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if problem:
        _.text(
            0.6,
            0.8,
            "\n".join(wrap(problem.upper(), 25)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if solution:
        _.text(
            0.51,
            0.2,
            "\n".join(wrap(solution.upper(), 40)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def fry(inter, text1: str = None, text2: str = None, _=None):
    if text1:
        _.text(
            0.51,
            0.8,
            "\n".join(wrap(text1.upper(), 55)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text2:
        _.text(
            0.51,
            0.2,
            "\n".join(wrap(text2.upper(), 55)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def gettingpaid(inter, text: str = None, _=None):
    if text:
        _.text(
            0.51,
            0.2,
            "\n".join(wrap(text.upper(), 55)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def goosebumps(inter, text: str = None, _=None):
    if text:
        _.text(
            0.52,
            0.8,
            "\n".join(wrap(text.upper(), 40)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def grandma(inter, text1: str = None, text2: str = None, _=None):
    if text1:
        _.text(
            0.52,
            0.83,
            "\n".join(wrap(text1.upper(), 50)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text2:
        _.text(
            0.52,
            0.2,
            "\n".join(wrap(text2.upper(), 50)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def grave(inter,text1: str = None, text2: str = None, _=None):
    if text1:
        _.text(
            0.39,
            0.6,
            "\n".join(wrap(text1.upper(), 30)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text2:
        _.text(
            0.6,
            0.3,
            "\n".join(wrap(text2.upper(), 30)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def handshake(inter, left: str = None, right: str = None, handshake: str = None, _=None):
    if left:
        _.text(
            0.3,
            0.4,
            "\n".join(wrap(left.upper(), 30)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if right:
        _.text(
            0.7,
            0.4,
            "\n".join(wrap(right.upper(), 30)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if handshake:
        _.text(
            0.5,
            0.7,
            "\n".join(wrap(handshake.upper(), 30)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def harold(inter, text1: str = None, text2: str = None, _=None):
    if text1:
        _.text(
            0.51,
            0.55,
            "\n".join(wrap(text1.upper(), 40)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text2:
        _.text(
            0.51,
            0.18,
            "\n".join(wrap(text2.upper(), 40)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def headout(inter, text1: str = None, text2: str = None, _=None):
    if text1:
        _.text(
            0.3,
            0.8,
            "\n".join(wrap(text1.upper(), 35)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="left",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text2:
        _.text(
            0.3,
            0.76,
            "\n".join(wrap(text2.upper(), 35)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="left",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def math(inter, text: str = None, _=None):
    if text:
        _.text(
            0.3,
            0.55,
            "\n".join(wrap(text.upper(), 35)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def pooh(inter, text1: str = None, text2: str = None, _=None):
    if text1:
        _.text(
            0.65,
            0.7,
            "\n".join(wrap(text1.upper(), 32)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text2:
        _.text(
            0.65,
            0.3,
            "\n".join(wrap(text2.upper(), 32)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def samepic(inter, text1: str = None, text2: str = None, _=None):
    if text1:
        _.text(
            0.65,
            0.7,
            "\n".join(wrap(text1.upper(), 20)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text2:
        _.text(
            0.4,
            0.75,
            "\n".join(wrap(text2.upper(), 20)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def scientist(inter, text: str = None, _=None):
    if text:
        _.text(
            0.5,
            0.26,
            "\n".join(wrap(text.upper(), 70)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def skeptical(inter, text1: str = None, text2: str = None, _=None):
    if text1:
        _.text(
            0.5,
            0.8,
            "\n".join(wrap(text1.upper(), 40)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    if text2:
        _.text(
            0.5,
            0.2,
            "\n".join(wrap(text2.upper(), 40)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def think(inter, text: str = None, _=None):
    if text:
        _.text(
            0.5,
            0.26,
            "\n".join(wrap(text.upper(), 70)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _

@create_and_send_meme()
def uno(inter, text: str = None, _=None):
    if text:
        _.text(
            0.42,
            0.6,
            "\n".join(wrap(text.upper(), 20)),
            fontsize=16,
            color="white",
            alpha=0.9,
            horizontalalignment="center",
            verticalalignment="center",
            path_effects=[pe.withStroke(linewidth=4, foreground="black")]
        )
    return _


bot.run(DISCORD_BOT_API_KEY)
