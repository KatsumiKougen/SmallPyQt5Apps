# Code borrowed from: https://wiki.python.org/moin/PyQt/Python%20syntax%20highlighting
# Thanks for the code! You guys are awesome!

from PyQt5 import QtWidgets, QtCore, QtGui

def TE_Format(RGBValue: list[int, int, int] | tuple[int, int, int], Bold: bool = False, Italic: bool = False):
    col = QtGui.QColor()
    col.setRgb(*RGBValue)
    
    format_ = QtGui.QTextCharFormat()
    format_.setForeground(col)
    if Bold:
        format_.setFontWeight(QtGui.QFont.Bold)
    if Italic:
        format_.setFontItalic(True)
    
    return format_

class TE_HighlightStyle:

    Python = 0

TE_GlobalStyles = {
    'keyword': TE_Format([209, 40, 201], Bold=True),
    'operator': TE_Format([159, 175, 179]),
    'brace': TE_Format([255, 243, 15]),
    'defclass': TE_Format([56, 99, 217], Bold=True),
    'string': TE_Format([232, 97, 39], Italic=True),
    'string2': TE_Format([232, 97, 39], Italic=True),
    'comment': TE_Format([83, 140, 52]),
    'self': TE_Format([83, 140, 52], Bold=True),
    'numbers': TE_Format([177, 217, 137]),
}

class TE_Highlighter(QtGui.QSyntaxHighlighter):
    
    def __init__(self, lang: int, parent: QtGui.QTextDocument):
        super().__init__(parent)
    
        self.SyntaxRules = {}
        match lang:
            case TE_HighlightStyle.Python:
                # Python keywords
                self.SyntaxRules["keywords"] = [
                    'and', 'assert', 'break', 'class', 'continue', 'def',
                    'del', 'elif', 'else', 'except', 'exec', 'finally',
                    'for', 'from', 'global', 'if', 'import', 'in',
                    'is', 'lambda', 'not', 'or', 'pass', 'print',
                    'raise', 'return', 'try', 'while', 'yield',
                    'None', 'True', 'False',
                ]

                # Python operators
                self.SyntaxRules["operators"] = [
                    '=',
                    # Comparison
                    '==', '!=', '<', '<=', '>', '>=',
                    # Arithmetic
                    '\+', '-', '\*', '/', '//', '\%', '\*\*',
                    # In-place
                    '\+=', '-=', '\*=', '/=', '\%=',
                    # Bitwise
                    '\^', '\|', '\&', '\~', '>>', '<<',
                ]

                # Python braces
                self.SyntaxRules["braces"] = [
                    '\{', '\}', '\(', '\)', '\[', '\]',
                ]
                
                # Multi-line strings (expression, flag, style)
                self.tri_single = (QtCore.QRegExp("'''"), 1, TE_GlobalStyles['string2'])
                self.tri_double = (QtCore.QRegExp('"""'), 2, TE_GlobalStyles['string2'])

                rules = []

                # Keyword, operator, and brace rules
                rules += [(r'\b%s\b' % w, 0, TE_GlobalStyles['keyword']) for w in self.SyntaxRules["keywords"]]
                rules += [(r'%s' % o, 0, TE_GlobalStyles['operator']) for o in self.SyntaxRules["operators"]]
                rules += [(r'%s' % b, 0, TE_GlobalStyles['brace']) for b in self.SyntaxRules["braces"]]

                # All other rules
                rules += [
                    # 'self'
                    (r'\bself\b', 0, TE_GlobalStyles['self']),

                    # 'def' followed by an identifier
                    (r'\bdef\b\s*(\w+)', 1, TE_GlobalStyles['defclass']),
                    # 'class' followed by an identifier
                    (r'\bclass\b\s*(\w+)', 1, TE_GlobalStyles['defclass']),

                    # Numeric literals
                    (r'\b[+-]?[0-9]+[lL]?\b', 0, TE_GlobalStyles['numbers']),
                    (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, TE_GlobalStyles['numbers']),
                    (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, TE_GlobalStyles['numbers']),

                    # Double-quoted string, possibly containing escape sequences
                    (r'"[^"\\]*(\\.[^"\\]*)*"', 0, TE_GlobalStyles['string']),
                    # Single-quoted string, possibly containing escape sequences
                    (r"'[^'\\]*(\\.[^'\\]*)*'", 0, TE_GlobalStyles['string']),

                    # From '#' until a newline
                    (r'#[^\n]*', 0, TE_GlobalStyles['comment']),
                ]

                # Build a QRegExp for each pattern
                self.rules = [(QtCore.QRegExp(pat), index, fmt) for (pat, index, fmt) in rules]
    
    def highlightBlock(self, text):
        """Apply syntax highlighting to the given block of text.
        """
        self.tripleQuoutesWithinStrings = []
        # Do other syntax formatting
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)
            if index >= 0:
                # if there is a string we check
                # if there are some triple quotes within the string
                # they will be ignored if they are matched again
                if expression.pattern() in [r'"[^"\\]*(\\.[^"\\]*)*"', r"'[^'\\]*(\\.[^'\\]*)*'"]:
                    innerIndex = self.tri_single[0].indexIn(text, index + 1)
                    if innerIndex == -1:
                        innerIndex = self.tri_double[0].indexIn(text, index + 1)

                    if innerIndex != -1:
                        tripleQuoteIndexes = range(innerIndex, innerIndex + 3)
                        self.tripleQuoutesWithinStrings.extend(tripleQuoteIndexes)

            while index >= 0:
                # skipping triple quotes within strings
                if index in self.tripleQuoutesWithinStrings:
                    index += 1
                    expression.indexIn(text, index)
                    continue

                # We actually want the index of the nth match
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        # Do multi-line strings
        in_multiline = self.MatchMultiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.MatchMultiline(text, *self.tri_double)

    def MatchMultiline(self, text, delimiter, in_state, style):
        """Do highlighting of multi-line strings. ``delimiter`` should be a
        ``QRegExp`` for triple-single-quotes or triple-double-quotes, and
        ``in_state`` should be a unique integer to represent the corresponding
        state changes when inside those strings. Returns True if we're still
        inside a multi-line string when this function is finished.
        """
        # If inside triple-single quotes, start at 0
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        # Otherwise, look for the delimiter on this line
        else:
            start = delimiter.indexIn(text)
            # skipping triple quotes within strings
            if start in self.tripleQuoutesWithinStrings:
                return False
            # Move past this match
            add = delimiter.matchedLength()

        # As long as there's a delimiter match on this line...
        while start >= 0:
            # Look for the ending delimiter
            end = delimiter.indexIn(text, start + add)
            # Ending delimiter on this line?
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            # No; multi-line string
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add
            # Apply formatting
            self.setFormat(start, length, style)
            # Look for the next match
            start = delimiter.indexIn(text, start + length)

        # Return True if still inside a multi-line string, False otherwise
        if self.currentBlockState() == in_state:
            return True
        else:
            return False
