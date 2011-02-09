import re

from markdown.preprocessors import Preprocessor
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, TextLexer


class CodeBlockPreprocessor(Preprocessor):

    pattern = re.compile(
        r'\[sourcecode:(.+?)\](.+?)\[/sourcecode\]', re.S)

    def run(self, lines):
        def repl(m):
            try:
                lexer = get_lexer_by_name(m.group(1))
            except ValueError:
                lexer = TextLexer()
            code = highlight(m.group(2), lexer, HtmlFormatter())
            code = code.replace('\n\n', '\n&nbsp;\n')
            return '\n\n<div class="code">%s</div>\n\n' % code
        return self.pattern.sub(
            repl, '\n'.join(lines)).split('\n')