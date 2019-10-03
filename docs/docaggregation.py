import os, re, subprocess, sys
from docutils import nodes, statemachine
from docutils.parsers.rst import Directive, directives
from sphinx.util.compat import directive_dwim

class DocFetch(Directive):

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False

    def _setup_repo(self, repo):
        env = self.state.document.settings.env
        path = os.path.normpath(env.doc2path(env.docname, base=None))
        cache = os.path.join(os.path.dirname(path), '_docfetch')
        root = os.path.join(cache, re.sub('[\W\-]+', '_', repo))
        if not os.path.exists(root):
            os.makedirs(root)
        subprocess.call(['svn', 'co', repo, root])
        return root

    def run(self):
        root = self._setup_repo(self.arguments[0])
        for path in self.content:
            data = open(os.path.join(root, path), 'rb').read()
            lines = statemachine.string2lines(data)
            self.state_machine.insert_input(lines, path)
        return []

def setup(app):
    app.add_directive('docaggregation', directive_dwim(DocFetch))
