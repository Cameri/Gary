"""
chatlog.py: written by MikeFightsBears 2013
"""

import datetime
import time
from util import hook, timesince


@hook.command
def last(inp, nick='', input=None, db=None, say=None):
    ".last <phrase> - finds the last occurence of a phrase"
    regex_msg = '%' + inp.strip() + '%'
    row = db.execute("select time, nick, msg, uts from log where msg like ?"
        " and uts = (select max(uts) from log where msg like ? and"
        " uts != (select max(uts) from log where msg like ?))"
        " and chan = ?",
        (regex_msg, regex_msg, regex_msg, input.chan)).fetchone()
    if row:
        if row[1] == 'asdf':#nick:
            say("Seriously? You said it like, just now...")
        elif row[0] == 'not this':
            say("Seriously? %s said it like, just now..." % row[1])
        else:
            say("%s last said \"%s\" on %s (%s ago)" %
                (row[1], row[2], row[0][:-7], timesince.timesince(row[3])))
    else:
        say("Never!")


@hook.command
def first(inp, input=None, db=None, say=None):
    ".first <phrase> - finds the first occurence of a phrase"
    regex_msg = '%' + inp.strip() + '%'
    row = db.execute(
        "select time, nick, msg, uts from log where msg like ? and uts = (select min(uts) from log where msg like ? ) and chan = ?",
        (regex_msg, regex_msg, input.chan)).fetchone()
    if row:
        say("%s first said \"%s\" on %s (%s ago)" %
            (row[1], row[2], row[0][:-7], timesince.timesince(row[3])))
    else:
        say("Never!")


@hook.command(autohelp=False)
def king(inp, input=None, db=None, say=None, bot=None):
    ".king - gets the user with the most used commands"
    query_string = "select nick, count(nick) as nick_occ from log where ("
    for command in bot.commands.keys():
        query_string = query_string + "msg like '." + command + "%' or "
    query_string = query_string.strip('or ')
    query_string = query_string + ") and nick != 'bears' "
    query_string = query_string + \
        "and chan = '%s' group by nick order by nick_occ desc limit 2;" % input.chan
    rows = db.execute(query_string).fetchall()

    if len(rows) == 2:
        say("%s is the king of %s with %s commands. %s is the runner up with %s commands." %
            (rows[0][0], input.conn.nick, rows[0][1], rows[1][0], rows[1][1]))
    elif len(rows) == 1:
        say("%s is the king of %s with %s commands." %
            (rows[0][0], input.conn.nick, rows[0][1]))
    else:
        say("No one has used my commands yet in this channel :(")


@hook.command
def said(inp, input=None, db=None, say=None):
    ".said <phrase> - finds anywho who has said a phrase"
    regex_msg = '%' + inp.strip() + '%'
    rows = db.execute(
        "select distinct nick from log where msg like ? and chan = ? order by nick",
        (regex_msg, input.chan)).fetchall()
    if rows:
        raw_list = ""
        overflow_counter = 0
        for row in rows:
            return_string = "%s have said %s" % (raw_list[:-2], input.msg[6:])
            if len(regex_msg) + len(return_string) + len(str(overflow_counter)) < 450:
                raw_list += row[0] + ", "
            else:
                overflow_counter += 1
        if overflow_counter == 0 and len(rows) == 1:
            return_string = "%s has said \"%s\"" % (
                raw_list[:-2], input.msg[6:])
        elif overflow_counter == 0 and len(rows) > 1:
            return_string = "%s have said \"%s\"" % (
                raw_list[:-2], input.msg[6:])
        else:
            return_string = "%s%s others have all said \"%s\"" % (
                raw_list, overflow_counter, input.msg[6:])
        formatted_string = rreplace(return_string, ', ', ', and ', 1)
        say(formatted_string)
    else:
        say("No one!")


def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

# def userstats():

# def dailylines():

# def dailystats():

# def lines():
