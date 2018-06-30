Django Postman
==============

*Downloaded from official repository on 2018/06/30.*

Django Postman isnt availlable on github.
The original project is on Bitbucket (mercurial folder =/= git ) : https://bitbucket.org/psam/django-postman

*NB:* the doc is supposed to be availlable in many language (as the text says on his wiki) but when we asked the author where were the others languages, he mocked us and said that "_it's time to learn english if you want to computer_"
well then, i don't even know why he even lies on his wiki :speak_no_evil: : https://bitbucket.org/psam/django-postman/wiki/Home maybe one day he will upload em.

Sad but still a good application if you use django ! 

**The following text is the official readme :**
--------------

<br />

This is an application for the Django web framework.

It provides a messaging functionality, mainly for a User-to-User exchange,
and with these convenient features:
- A non-User (email is undisclosed) can write to a User and get a reply
  (can be disabled by configuration)
- Exchanges can be moderated (with auto-accept and auto-reject plug-ins)
- Optional recipient filter plug-ins
- Optional exchange filtering plug-ins (blacklists)
- Multi-recipient writing is possible (can be disabled by configuration)
  with min/max constraints
- Messages are managed by conversations
- Messages in folders are sortable by sender|recipient|subject|date
- 'Archives' folder in addition to classic Inbox, Sent and Trash folders
- A Quick-Reply form to only ask for a response text
- A cleanup management command to clear the old deleted messages

It has support for optional additional applications:
- Autocomplete recipient field (default is 'django-ajax-selects'),
  with multiple recipient management
- New message notification (default is 'django-notification')
- Asynchronous mailer (default is 'django-mailer')

See the docs/ directory for Sphinx documentation.
For example, build the HTML version with >make html
and open docs/_build/html/index.html

Copyright (C) 2010, Patrick Samson
This program is licensed under the BSD License (see the file LICENSE).
