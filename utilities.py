from emoji import UNICODE_EMOJI_ALIAS_ENGLISH

def is_emoji(s):
    count = 0
    for emoji in UNICODE_EMOJI_ALIAS_ENGLISH:
        count += s.count(emoji)
        if count > 1:
            return False
    return bool(count)