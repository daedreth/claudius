# claudius
Are you tired of the discord developers using the gtk filepicker without image previews in the GNU/Linux release of the Discord client?

Me too. Luckily, even I can dedicate a few minutes to write a better alternative.

# Usage

You need qt4(or qt5), python3.5(or higher), imagemagick, ranger, discord.py and a terminal emulator installed.

Note: If you only plan to use selected features, then you obviously do not need certain dependencies.

  ~~~ sh
  $ git clone https://github.com/daedreth/claudius.git
  $ cd claudius
  $ make
  $ sudo make install
  ~~~

Edit `~/.config/claudius/config.ini` before launching the program accordingly.

Your token can be retrieved from the client, just search for how to find it.

The commands can be pretty much anything, edit them to suit your liking.

Just type `claudius` in a shell and watch some magic happen. Alternatively launch claudius by other means, if you are not big on debug messages.

Once you type your command in any channel or any private message, the appropriate action will take place.

# Image previews

Don't even get me started on the Discord devs using the gtk filepicker by default, but by some hacky adjustments to the QFileDialog or the awesomeness that ranger is, we now have previews.

# License
It's GPL-3, but it's just a little script.

Do what you must.
