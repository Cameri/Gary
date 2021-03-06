from util import hook, http, web


@hook.command(autohelp=False)
def rfact(inp, say=False, nick=False):
    """.rfact - Gets a random fact from OMGFACTS."""

    attempts = 0

    # all of this is because omgfacts is fail
    while True:
        try:
            soup = http.get_soup('http://www.omg-facts.com/random')
        except:
            if attempts > 2:
                return "Could not find a fact!"
            else:
                attempts += 1
                continue

        response = soup.find('a', {'class': 'surprise'})
        link = response['href']
        fact = ''.join(response.find(text=True))

        if fact:
            fact = fact.strip()
            break
        else:
            if attempts > 2:
                return "Could not find a fact!"
            else:
                attempts += 1
                continue

    url = web.try_googl(link)

    return "{} - {}".format(fact.encode('ascii', 'ignore'), url)
