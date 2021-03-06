# Discord Memes

<img width="1310" alt="Screenshot 2022-07-04 at 01 54 43" src="https://user-images.githubusercontent.com/25267873/177064233-0dffc6b6-60a7-4b9d-bca6-c0f8158b8cc7.png">

The idea of this Discord Memes is to avoid to open [imgflip](https://imgflip.com) everytime you want to add text to a meme. Personally, I love gifs available through Discord but I feel like sometimes a meme with text is much more powerful.

I felt the [OpenBB Community](https://github.com/OpenBB-finance/OpenBBTerminal) was in need of something like this. So this bot is running on Heroku on [OpenBB Discord](https://discord.gg/kGcmve8Ekw). Try it out now!

## Usage

1. Add the meme you want to the `memes/` folder, e.g. `spongebob.jpg`
2. Then create a function with the same name of the image (e.g. `spongebob`) with the following format

```
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
```

3. That's it.

Note: I created a decorator `@create_and_send_meme()` that basically abstracts all the meme creation and picks up the image on memes with the same name of the function. This way, the person adding a meme just needs to focus on the text on the image, i.e. it's location, size, where it wraps, colors and alignment.
