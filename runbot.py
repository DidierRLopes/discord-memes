import os
import uuid
import disnake
from disnake.ext import commands
import pyimgur
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from textwrap import wrap
from random import choice
import functools

DISCORD_BOT_API_KEY = ""
IMGUR_API_KEY = ""
TEST_GUILD = 0
plt.rcParams["font.family"] = "impact"

bot = commands.Bot(test_guilds=[TEST_GUILD], sync_commands_debug=True)
memes_imgur = pyimgur.Imgur(IMGUR_API_KEY)

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
            image_path = f"{kwargs['inter'].data.name}.jpg".replace(".jpg", f"_{str(uuid.uuid1()).replace('-', '')}.jpg")
            plt.savefig(image_path, bbox_inches='tight', transparent=True, pad_inches=0)
            plt.close("all")
            image = disnake.File(image_path)
            embed.set_image(url=f"attachment://{image_path}")
            os.remove(image_path)

            await kwargs['inter'].send(embed=embed, file=image)

        return wrapped
    return wrapper


@create_and_send_meme()
def spongebob(inter, text: str, _=None):
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
def chloe(inter, text: str, _=None):
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
def dogecheems(inter, dogename: str, dogetext:str, cheemsname: str, cheemstext: str, _=None):
    _.text(
        0.25,
        0.9,
        "\n".join(wrap(dogename.upper(), 20)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.25,
        0.2,
        "\n".join(wrap(dogetext.upper(), 20)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.75,
        0.2,
        "\n".join(wrap(cheemstext.upper(), 20)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.75,
        0.8,
        "\n".join(wrap(cheemsname.upper(), 20)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def stonks(inter, text: str, _=None):
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
def clown(inter, text1: str, text2: str, text3: str, text4: str, _=None):
    _.text(
        0.4,
        0.8,
        "\n".join(wrap(text1.upper(), 25)),
        fontsize=8,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.4,
        0.6,
        "\n".join(wrap(text2.upper(), 25)),
        fontsize=8,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.4,
        0.4,
        "\n".join(wrap(text2.upper(), 25)),
        fontsize=8,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.4,
        0.2,
        "\n".join(wrap(text2.upper(), 25)),
        fontsize=8,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _


@create_and_send_meme()
def conspiracy(inter, person: str, text: str, _=None):
    _.text(
        0.5,
        0.8,
        "\n".join(wrap(person.upper(), 60)),
        fontsize=8,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.5,
        0.2,
        "\n".join(wrap(text.upper(), 60)),
        fontsize=8,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def cryingkid(inter, kid: str, adult: str, text: str, _=None):
    _.text(
        0.5,
        0.65,
        "\n".join(wrap(kid.upper(), 35)),
        fontsize=8,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.5,
        0.4,
        "\n".join(wrap(adult.upper(), 35)),
        fontsize=8,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.5,
        0.18,
        "\n".join(wrap(text.upper(), 35)),
        fontsize=8,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def dicaprio(inter, text: str, _=None):
    _.text(
        0.5,
        0.2,
        "\n".join(wrap(text.upper(), 35)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _


@create_and_send_meme()
def disappointed(inter, text1: str, text2: str, _=None):
    _.text(
        0.35,
        0.7,
        "\n".join(wrap(text1.upper(), 35)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.35,
        0.3,
        "\n".join(wrap(text2.upper(), 35)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def dosomething(inter, text: str, _=None):
    _.text(
        0.55,
        0.7,
        "C'mon, do something",
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.55,
        0.25,
        "\n".join(wrap(text.upper(), 30)),
        fontsize=10,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def drake(inter, text1: str, text2: str, _=None):
    _.text(
        0.7,
        0.7,
        "\n".join(wrap(text1.upper(), 30)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.7,
        0.3,
        "\n".join(wrap(text2.upper(), 30)),
        fontsize=10,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def firedog(inter, text: str, _=None):
    _.text(
        0.33,
        0.7,
        "\n".join(wrap(text.upper(), 35)),
        fontsize=10,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def firegirl(inter, text1: str, text2: str, _=None):
    _.text(
        0.5,
        0.8,
        "\n".join(wrap(text1.upper(), 50)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.5,
        0.2,
        "\n".join(wrap(text2.upper(), 50)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def flextape(inter, person: str, problem: str, solution: str, _=None):
    _.text(
        0.42,
        0.6,
        "\n".join(wrap(person.upper(), 30)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.6,
        0.8,
        "\n".join(wrap(problem.upper(), 25)),
        fontsize=10,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.51,
        0.2,
        "\n".join(wrap(solution.upper(), 40)),
        fontsize=10,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )


    return _

@create_and_send_meme()
def fry(inter, text1: str, text2: str, _=None):
    _.text(
        0.51,
        0.8,
        "\n".join(wrap(text1.upper(), 55)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.51,
        0.2,
        "\n".join(wrap(text2.upper(), 55)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def gettingpaid(inter, text: str, _=None):
    _.text(
        0.51,
        0.2,
        "\n".join(wrap(text.upper(), 55)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def goosebumps(inter, text: str, _=None):
    _.text(
        0.52,
        0.8,
        "\n".join(wrap(text.upper(), 40)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def grandma(inter, text1: str, text2: str, _=None):
    _.text(
        0.52,
        0.83,
        "\n".join(wrap(text1.upper(), 50)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.52,
        0.2,
        "\n".join(wrap(text2.upper(), 50)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def grave(inter,text1: str, text2: str, _=None):
    _.text(
        0.39,
        0.6,
        "\n".join(wrap(text1.upper(), 30)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.6,
        0.3,
        "\n".join(wrap(text2.upper(), 30)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def handshake(inter, left: str, right: str, handshake: str, _=None):
    _.text(
        0.3,
        0.4,
        "\n".join(wrap(left.upper(), 30)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.7,
        0.4,
        "\n".join(wrap(right.upper(), 30)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.5,
        0.7,
        "\n".join(wrap(handshake.upper(), 30)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def harold(inter, text1: str, text2: str, _=None):
    _.text(
        0.51,
        0.55,
        "\n".join(wrap(text1.upper(), 40)),
        fontsize=10,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.51,
        0.18,
        "\n".join(wrap(text2.upper(), 40)),
        fontsize=10,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def headout(inter, text1: str, text2: str, _=None):
    _.text(
        0.3,
        0.8,
        "\n".join(wrap(text1.upper(), 35)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="left",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.3,
        0.76,
        "\n".join(wrap(text2.upper(), 35)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="left",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def math(inter, text: str, _=None):
    _.text(
        0.3,
        0.55,
        "\n".join(wrap(text.upper(), 35)),
        fontsize=10,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def pooh(inter, text1: str, text2: str, _=None):
    _.text(
        0.65,
        0.7,
        "\n".join(wrap(text1.upper(), 32)),
        fontsize=10,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.65,
        0.3,
        "\n".join(wrap(text2.upper(), 32)),
        fontsize=10,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def samepic(inter, text1: str, text2: str, _=None):
    _.text(
        0.65,
        0.7,
        "\n".join(wrap(text1.upper(), 20)),
        fontsize=10,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.4,
        0.75,
        "\n".join(wrap(text2.upper(), 20)),
        fontsize=10,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def scientist(inter, text: str, _=None):
    _.text(
        0.5,
        0.26,
        "\n".join(wrap(text.upper(), 70)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def skeptical(inter, text1: str, text2: str, _=None):
    _.text(
        0.5,
        0.8,
        "\n".join(wrap(text1.upper(), 40)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    _.text(
        0.5,
        0.2,
        "\n".join(wrap(text2.upper(), 40)),
        fontsize=10,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def think(inter, text: str, _=None):
    _.text(
        0.5,
        0.26,
        "\n".join(wrap(text.upper(), 70)),
        fontsize=12,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _

@create_and_send_meme()
def uno(inter, text: str, _=None):
    _.text(
        0.42,
        0.6,
        "\n".join(wrap(uno.upper(), 20)),
        fontsize=9,
        color="white",
        alpha=0.9,
        horizontalalignment="center",
        verticalalignment="center",
        path_effects=[pe.withStroke(linewidth=4, foreground="black")]
    )
    return _


bot.run(DISCORD_BOT_API_KEY)
