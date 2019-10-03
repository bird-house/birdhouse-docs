import os, re, subprocess
from docutils.parsers.rst.directives.misc import Include as BaseInclude
from sphinx.directives import TocTree
from sphinx.util.docutils import SphinxDirective


def checkout(env, repo, branch='master'):
    """Checkout git repository and return the relative path to the source directory."""

    cache = os.path.join(env.srcdir, '_gitext')
    root = os.path.join(cache, re.sub('[\W\-]+', '_', repo))

    # Clone the repo
    if not os.path.exists(root):
        os.makedirs(root)
        subprocess.run(['git', 'clone', '--depth=1', repo, root])

    # Fetch latest version and checkout branch
    subprocess.run(['git', 'fetch', repo], cwd=root)
    subprocess.call(['git', 'co', branch], cwd=root)

    return os.path.relpath(root, start=env.srcdir)


class GitTocTree(TocTree):
    """Table of content directive drawing from a git repository.

    Example
    -------
    .. gittoctree:: <https://url_to_git_repo>

       <relative_path_1>
       <relative_path_2>

    """
    required_arguments = 1

    def run(self):
        env = self.state.document.settings.env
        root = checkout(env, self.arguments[0])

        # Link the content to the cloned repository
        self.content = [os.path.join(root, content) for content in self.content]

        return super().run()


class GitInclude(BaseInclude, SphinxDirective):
    """Include directive for file fetched from a git repository.

    Arguments
    ---------
    repo : str
      HTTP url to the git repository.
    path : str
      Relative path to the file inside the repository.

    Example
    -------

    .. gitinclude:: <https://url_to_git_repo> <relative path to file>
    """
    required_arguments = 2

    def run(self):
        env = self.state.document.settings.env
        root = checkout(env, self.arguments[0])

        # Point path to the file in the cloned repo
        rel_filename, filename = self.env.relfn2path(os.path.join(root, self.arguments[1]))
        self.arguments = [filename]
        self.env.note_included(filename)
        return super().run()


def setup(app):
    app.add_directive('gitinclude', GitInclude)
    app.add_directive('gittoctree', GitTocTree)
