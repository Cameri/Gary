from util import hook, http


@hook.command
def imdb(inp):
    """.imdb <movie> - gets information about <movie> from IMDb."""

    try:
        content = http.get_json("http://www.omdbapi.com/", t=inp)
    except:
        return "API timeout, please try again in a few seconds."

    if content['Response'] == 'Movie Not Found':
        return 'Movie not found.'
    elif content['Response'] == 'True':
        content['URL'] = 'http://www.imdb.com/title/%(imdbID)s' % content

        out = '\x02%(Title)s\x02 (%(Year)s) (%(Genre)s): %(Plot)s'
        if content['Runtime'] != 'N/A':
            out += ' \x02%(Runtime)s\x02.'
        if content['imdbRating'] != 'N/A' and content['imdbVotes'] != 'N/A':
            out += ' \x02%(imdbRating)s/10\x02 with \x02%(imdbVotes)s\x02 votes.'
        out += ' %(URL)s'
        return out % content
    else:
        return 'Unknown error.'
