TYPES = {
    0: 'missed',
    1: 'received',
    2: 'voicemail',
    4: 'recorded',
    7: 'placed',
    10: 'sms.received',
    11: 'sms.sent'
}

DEBUG = False
LOGIN = 'https://accounts.google.com/ServiceLogin?service=grandcentral'
SMSAUTH = 'https://accounts.google.com/SmsAuth'
FEEDS = ('inbox', 'starred', 'all', 'spam', 'trash', 'voicemail', 'sms',
        'recorded', 'placed', 'received', 'missed')

BASE = 'https://www.google.com/voice/b/0/'
LOGOUT = 'https://www.google.com/voice/account/signout'
INBOX = BASE + '#inbox'
CALL = BASE + 'call/connect/'
CANCEL = BASE + 'call/cancel/'
DEFAULT_FORWARD = BASE + 'settings/editDefaultForwarding/'
FORWARD = BASE + 'settings/editForwarding/'
DELETE = BASE + 'inbox/deleteMessages/'
ARCHIVE = BASE + 'inbox/archiveMessages/'
MARK = BASE + 'inbox/mark/'
STAR = BASE + 'inbox/star/'
SMS = BASE + 'sms/send/'
DOWNLOAD = BASE + 'media/send_voicemail/'
BALANCE = BASE + 'settings/billingcredit/'

XML_SEARCH = BASE + 'inbox/search/'
XML_CONTACTS = BASE + 'contacts/'
XML_RECENT = BASE + 'inbox/recent/'
XML_MESSAGE = BASE + 'inbox/message/'
XML_INBOX = XML_RECENT + 'inbox/'
XML_STARRED = XML_RECENT + 'starred/'
XML_ALL = XML_RECENT + 'all/'
XML_SPAM = XML_RECENT + 'spam/'
XML_TRASH = XML_RECENT + 'trash/'
XML_VOICEMAIL = XML_RECENT + 'voicemail/'
XML_SMS = XML_RECENT + 'sms/'
XML_RECORDED = XML_RECENT + 'recorded/'
XML_PLACED = XML_RECENT + 'placed/'
XML_RECEIVED = XML_RECENT + 'received/'
XML_MISSED = XML_RECENT + 'missed/'
