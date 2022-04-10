Krita scripts
=============

This repository is intended to collect Krita plugins I wrote to fill certain
personal needs.  More may be added in the future as the need arises.


Installation
------------

 1. Copy the `actions` and `pykrita` directories in this repository to the Krita
    resources folder.  You can locate the resources folder by going to
    Settings > Manage Resources… > Open Resource Folder in Krita.
 2. Afterwards, go to Settings > Configure Krita… > Python Plugin Manager and
    enable the plugins you need.


Brush Sizer (brushsizer)
------------------------

Defines two actions for increasing and decreasing the current brush size in
intelligent increments by taking bigger steps when the brush size is bigger.
Mimics the behaviour of a certain popular digital painting program.

Provides:
 - Tools > Scripts > Increase Brush Size (Smart)
 - Tools > Scripts > Decrease Brush Size (Smart)

The default keybindings are <kbd>[</kbd> and <kbd>]</kbd>, but they can be
changed in the Keyboard Shortcuts section of the Krita settings.
