class script(object):
    START_TXT = """<b>Heyy {}.
I'm Millie Bobby Brown :)
I was Actually Made for <a href=https://t.me/CinemaGround>CinemaGround</a>

Add me to your Groups & Enjoy!
Tap <code>Help</code> If you have any Doubt about how to use me in your Groups!</b>"""
    HELP_TXT = """ππππ : <b>How to use me?</b>

- Add me to your Group, Promote me as an Admin. 

That's it! <b>Bot is now Ready!</b>

<a href='http://t.me/ZaynAndMillie'>π πΆπΉπΉπΆπ²</a>"""
    ABOUT_TXT = """π€ πππ : <a href=https://t.me/ZaynAndMillie>π πππππ</a>

π¨βπ» πππππππ : <a href=https://t.me/axnzal>ππ¨π ππ‘</a>

π πππππππ : <a href=https://github.com/pyrogram/pyrogram>π£π¬π₯π’ππ₯ππ </a>

π ππππππππ : <a href=https://www.python.org/>π£π¬π§ππ’π‘</a>

π‘ πππ ππππππ : <a href=http://google.com/>ππ‘π§ππ₯π‘ππ§</a>

π ππππππππ : <a href=https://www.mongodb.com/>π π’π‘ππ’ ππ</a>

π£ πππππππ πππππππ : <a href=https://t.me/ZaynAndMillie>π πππππ π¨π£πππ§ππ¦</a>

π€ πππππππ : <a href=https://t.me/XaynBot>π­ππ¬π‘</a>"""
    SOURCE_TXT = """ππππ : <b>Source Code</b>

- Millie Bot is a Private Source Project.

<a href='http://t.me/ZaynAndMillie'>π πΆπΉπΉπΆπ²</a>"""
    MANUELFILTER_TXT = """ππππ : <b>Filters</b>

- Filter is the feature were users can set automated Replies for a particular keyword and Millie will respond whenever a keyword is found in the message.


ππππ :

β <b>Millie Bot</b> should have Admin.
β Only <b>Admins</b> can Add filters in the Connected chat.
β Alert buttons have a limit of <b>64 characters.</b>


ππππππππ πππ πππππ :

β /filter - <code>Adds a filter in the Connected Chat.</code>
β /viewfilters - <code>Lists all the filters of the Connected Chat.</code>
β /delf - <code>Deletes a Specific Filter in the Connected Chat.</code>
β /delallf - <code>Deletes the whole Filters in the Connected Chat ( For Chat Owner Only ).</code>

<a href='http://t.me/ZaynAndMillie'>π πΆπΉπΉπΆπ²</a>"""
    BUTTON_TXT = """ππππ : <b>Buttons</b>

- Millie Supports Both URL and ALERT Inline Buttons.


ππππ :

β <b>Millie</b> supports buttons with any telegram media type.
β Telegram will not Allows you to send Buttons Without any <b>Content</b>, So Content is Mandatory.
β Buttons should be properly parsed as <b>Markdown format.</b>


πππππππ πππππ :

β <b>URL Buttons :</b>
<code>[Button Text](buttonurl:https://t.me/CGProBot)</code>

β <b>Alert Buttons :</b>
<code>[Button Text](buttonalert:This is an Alert message)</code>

<a href='http://t.me/ZaynAndMillie'>π πΆπΉπΉπΆπ²</a>"""
    AUTOFILTER_TXT = """ππππ : <b>Auto Filter</b>

β Make me the <b>Admin</b> of your channel if it's private.
β Make sure that your Channel does not contains <b>Camrips, Porn or Fake </b>files.
β <b>Forward</b> the last message to me with quotes. I'll Add all the files in that channel to my <b>DataBase.</b>

<a href='http://t.me/ZaynAndMillie'>π πΆπΉπΉπΆπ²</a>"""
    CONNECTION_TXT = """<b>ππππ : <b>Connections</b>

- Used to connect Bot to PM for managing filters.
- It helps to avoid spamming in groups.


ππππ :

β Only admins can Add a connection.
β Send <code>/connectit</code> in your Group for connecting me to your PM. ( Only After making me Admin )


ππππππππ πππ πππππ :

β /connectit  - <code>Connect a Particular chat to your PM.</code>
β /disconnectit  - <code>Disconnect from a Particular Chat.</code>
β /myconnections - <code>List of all your Connections.</code></b>

<a href='http://t.me/ZaynAndMillie'>π πΆπΉπΉπΆπ²</a>"""
    EXTRAMOD_TXT = """ππππ : <b>Extra Modules</b>

- These are the Extra Features of Millie


ππππππππ πππ πππππ :

β /id - <code>Gets ID of a Specifed User.</code>
β /info  - <code>Gets Information About a Specifed User.</code>
β /imdb | /search - <code>Get the Movie Information From Various Sources.</code>

<a href='http://t.me/ZaynAndMillie'>π πΆπΉπΉπΆπ²</a>
"""
    ADMIN_TXT = """<b>Oh Yeah, Wait for It!</b>"""
    STATUS_TXT = """Β» π§π’π§ππ πππππ¦ : <code>{}</code>
Β» π§π’π§ππ π¨π¦ππ₯π¦ : <code>{}</code>
Β» π§π’π§ππ ππππ§π¦ : <code>{}</code>
Β» π¨π¦ππ π¦π§π’π₯πππ : <code>{}</code>
Β» ππ₯ππ π¦π§π’π₯πππ : <code>{}</code>

<a href='http://t.me/ZaynAndMillie'>π πΆπΉπΉπΆπ²</a>"""
    LOG_TEXT_G = """#NewGroup
Group - {} (<code>{}</code>)
Total Members - <code>{}</code>
Added By - {}

π πΆπΉπΉπΆπ²
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}

π πΆπΉπΉπΆπ²
"""
