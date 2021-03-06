from util import hook, http
import re


@hook.command(autohelp=False)
def kernel(inp, reply=None):
    """.kernel - Displays recent kernel versions."""
    contents = http.get("https://www.kernel.org/finger_banner")
    contents = re.sub(r'The latest(\s*)', '', contents)
    contents = re.sub(r'version of the Linux kernel is:(\s*)', '- ', contents)
    lines = contents.split("\n")

    message = "Linux kernel versions: "
    message += ", ".join(line for line in lines[:-1])
    reply(message)
