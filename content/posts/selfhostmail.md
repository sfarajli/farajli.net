---
title: "Hosting an email server is not possible."
slug: "hosting-email-server"
created: 2025-01-24
description: "Explaining why don't host an email server."
tags: [Technology]
draft: false
---

### Reasons to not host your own email server.

Last summer, I had successfully managed to host my email server but 
a couple of days ago I completely removed everything from my server
and purchased an email hosting service.

I'd like to share my experience with hosting an email server
and what makes the process an absolute nightmare.

#### - It's hard to find an affordable VPS provider that doesn't block port 25. 

If you don't know anything about email, you need the port 25 to be open to send mails but 
most server providers block it to reduce spam and the ones that don't costs more than
the usual ones.

#### - Getting a domain and IP that is not blacklisted.

If you have already bought a domain it might be blacklisted meaning that 
all the mails you'll send is going to go right into the spam folder of the receiver.
It's the same for IP but chaining it is a lot easier than getting a new domain on most 
server providers.

#### - Not enough documentation is available and some is outdated.

There isn't that much documentation for setting up an email server, I think that is
partially because of the process being so tough that no one really wants to document it 
and there are so many commands involved in the process
even just a small update on one program can make the documentation outdated.

#### - It's very hard to set up.
Configuring an email server was perhaps the hardest thing that I'd ever done 
(even after finding the proper documentation), I spent weeks on that.

#### - Almost certainly, your mails won't be delivered.

Even after going through the very difficult process of finding the correct server provider, 
documentation and setting everything up (DKIM, SPF etc.) you'll still end up in spams,
you might be able to pass spam filters of some email services, but you'll never feel 
confident of sending mails because big email services sometimes update their spam filters
and you got to keep up with those as well, so it doesn't just end there when you set it up.

#### Summing it up

I'd gladly host an email server, but I just can't make it work half as good as the paid 
email service providers. In the future I might try to do it again 
(though I don't think the results will be different) but now I'll stick to email services.
