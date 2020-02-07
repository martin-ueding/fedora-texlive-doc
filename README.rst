.. Copyright © 2016-2017 Martin Ueding <martin-ueding.de>

##################
fedora-texlive-doc
##################

On Fedora, each LaTeX package has its own RPM package. The naming scheme is
``texlive-PACKAGE``. Most LaTeX packages have a documentation PDF that one can
read with ``texdoc``. It needs to be separately installed with a package named
``texlive-PACKAGE-doc``.

Unfortunately I have not installed the documentation for the packages that I
have installed so far. Also in my Ansible playbooks I did not explicitly
mention the documentation packages. This Python program will use ``rpm`` to get
a list of all installed LaTeX RPM packages, add the ``-doc`` and check whether
that is a package that exists. This check takes about a second per package,
therefore the whole programs runs like half an hour. Perhaps one can speed it
up by using the Python bindings for the dnf package manager.

Once all that is finished, one can then install all the documentation package.
