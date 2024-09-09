<!-- Title: Why I prefer Gentoo -->

Why I prefer Gentoo over Arch.
------------------------------
A lot of people say very good things about gentoo linux, it is very well maintained,
It is more secure, It is lightweight and so on. But when it comes down to it,
very few people actuall use gentoo, I thing that is because they install it 
and after a month or so they really get sick of waiting for the packages to compile 
and they switch back to whatever they were using before. I know it becuase,
I had done that in the past, I dual-booted my machine with gentoo and arch linux
intending to only use gentoo, and arch only when I didn't have the time to wait
for the package to compile, but ended up only booting to arch and almost never 
to gentoo, at that time if you were to ask me the best package manager 
I would have unhesitantly said arch's pacman, while I still thing that pacman is the best 
<strong class="color1">binary</strong> package manager
for the past few months I have started to really like gentoo and its package manager,
portage and there are different reasons for that.   

### Compiling programs makes more sense than downloading.
On unix like operating systems you generally use 
open-source software and that software is made to be compiled by the users specific 
to their machines, but on binary based distros you use programs that are compiled for
you by someone else and again to me, personally compiling just makes more sense.

### It gives you more pespective of the program you use.
If you'd downloaded a binary package you would only be able to tell if a program is fast, 
has enough features and so on, but you wouldn't have known how much time it takes 
to compile, what the build dependencies are, and even sometimes the
programming language that it is written in. I do agree that knowing those abstract details 
of a package is utterly useless for a typical end-user who is not a programmer
but for a programmer those details are very important, since you get to know what build systems are
faster what programming language compiles faster, builds better and sometimes you learn 
about things that didn't even know existed. You can build programs from source in other distros
as well but gentoo makes it easier and forces you to do that
and be honest, If you could install binary package in 10 seconds
you wouldn't even bother compile it from the source.

### You install less packages.
In order to avoid compilation you tent to install less pieces of software
resulting in more stable and more performant system. God forbit you if
you are using arch linux and have access to the AUR 
(I had installed more than 2000 useless packages on my arch system). 

### It is more secure and faster and more lightweight (at least in theory).
I have not noticed any significant difference in terms of performance 
between gentoo and binary based distros and I kind of think that security 
on client OSes is overrated, but for some few people these might be important 
since you literally can skip some useless parts of a program (useless for you of course)
resulting in less bloated, therefore faster and more secure programs, but again I 
don't really find it that important.

### <strong class="color4">No systemd</strong>!
I am not against systemd but I prefer to not use it.
On gentoo the default init system is openrc and it works 
with no problem.


### Bad parts.
Like everything it has some negative stuff about it as well,
those are
* Compilation can take some time.
* Gentoo is the one of <strong class="color1">the hardest</strong> distro to manage.  
I am saying both of those with an asterisk, because 
although I agree that there are some big pieces software that you basically have to have 
like a browser, (it took 6h to compile a browser on my machine) most of the time
if a piece of software takes
much time to compile that indicates that piece of software is 
overcompilcated and shouldn't even be using that.  
Gentoo is hard to use but, that also means gentoo foces to know more that 
becomes a good thing.

So, that is all.
