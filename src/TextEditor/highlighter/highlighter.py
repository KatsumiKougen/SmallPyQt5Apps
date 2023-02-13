# Code borrowed from:
# - https://wiki.python.org/moin/PyQt/Python%20syntax%20highlighting
# - https://github.com/Secozzi/PyQt5-syntax-highlighting
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
    'keyword': TE_Format([237, 31, 227], Bold=True),
    'literals': TE_Format([74, 101, 255], Bold=True),
    'operator': TE_Format([185, 200, 201]),
    'brace': TE_Format([255, 210, 10]),
    'deffunc': TE_Format([74, 101, 255], Bold=True),
    'defclass': TE_Format([74, 101, 255], Bold=True),
    'string': TE_Format([217, 123, 80], Italic=True),
    'string2': TE_Format([217, 123, 80], Italic=True),
    'meta': TE_Format([46, 199, 53]),
    'special_attributes': TE_Format([255, 250, 110], Bold=True, Italic=True),
    'comment': TE_Format([56, 120, 48], Italic=True),
    'self': TE_Format([141, 210, 240], Bold=True),
    'numbers': TE_Format([148, 242, 133])
}

class TE_Highlighter(QtGui.QSyntaxHighlighter):
    
    def __init__(self, lang: int, parent: QtGui.QTextDocument):
        super().__init__(parent)
    
        self.SyntaxRules = {}
        match lang:
            case TE_HighlightStyle.Python:
                # Python keywords
                self.SyntaxRules["keywords"] = [
                    'and', 'as', 'assert', 'async', 'await',
                    'break',
                    'case', 'class', 'continue',
                    'def', 'del',
                    'elif', 'else', 'except',
                    'finally', 'for', 'from',
                    'global',
                    'if', 'import', 'in', 'is',
                    'lambda',
                    'match',
                    'nonlocal', 'not',
                    'or',
                    'pass',
                    'raise', 'return',
                    'try',
                    'while', 'with',
                    'yield'
                ]

                # Python operators
                self.SyntaxRules["operators"] = [
                    '=', '@'
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
                
                self.SyntaxRules["literals"] = [
                    'False', 'True', 'None'
                ]
                
                self.SyntaxRules["special_attributes"] = [
                    '__doc__', '__name__', '__qualname__',
                    '__module__', '__defaults__', '__code__',
                    '__globals__', '__dict__', '__closure__',
                    '__annotations__', '__kwdefaults__'
                ]
                
                self.SyntaxRules["class_dir"] = [
                    '__class__', '__delattr__', '__dict__',
                    '__dir__', '__doc__', '__eq__',
                    '__format__', '__ge__', '__getattribute__',
                    '__gt__', '__hash__', '__init__',
                    '__init_subclass__', '__le__', '__lt__',
                    '__module__', '__ne__', '__new__',
                    '__reduce__', '__reduce_ex__', '__repr__',
                    '__setattr__', '__sizeof__', '__str__',
                    '__subclasshook__', '__weakref__'
                ]
                
                self.SyntaxRules["types"] = [
                    'bool', 'int', 'float',
                    'complex', 'list', 'tuple',
                    'range', 'str', 'bytes',
                    'bytearray', 'memoryview',
                    'set', 'frozenset', 'dict'
                ]
                
                self.SyntaxRules["other"] = [
                    'super', 'append', 'extend',
                    'insert', 'remove', 'pop',
                    'clear', 'index', 'count',
                    'sort', 'reverse'
                ]
                
                # Multi-line strings (expression, flag, style)
                self.tri_single = (QtCore.QRegExp("'''"), 1, TE_GlobalStyles['string2'])
                self.tri_double = (QtCore.QRegExp('"""'), 2, TE_GlobalStyles['string2'])

                rules = []

                # Keyword, operator, and brace rules
                rules += [(f'\\b{w}\\b', 0, TE_GlobalStyles['keyword']) for w in self.SyntaxRules["keywords"]]
                rules += [(f'\\b{o}\\b', 0, TE_GlobalStyles['operator']) for o in self.SyntaxRules["operators"]]
                rules += [(f'\\b{b}\\b', 0, TE_GlobalStyles['brace']) for b in self.SyntaxRules["braces"]]
                
                rules += [(f'\\b{b}\\b', 0, TE_GlobalStyles['meta']) for b in self.SyntaxRules["other"]]
                rules += [(f'\\b{b}\\b', 0, TE_GlobalStyles['meta']) for b in self.SyntaxRules["types"]]
                rules += [(f'\\b{b}\\b', 0, TE_GlobalStyles['special_attributes']) for b in self.SyntaxRules["special_attributes"]]
                rules += [(f'\\b{b}\\b', 0, TE_GlobalStyles['meta']) for b in self.SyntaxRules["class_dir"]]
                rules += [(f'\\b{b}\\b', 0, TE_GlobalStyles['brace']) for b in self.SyntaxRules["braces"]]

                # All other rules
                rules += [
                    # 'self'
                    ('\\bself\\b', 0, TE_GlobalStyles['self']),

                    # 'def' followed by an identifier
                    ('\\bdef\\b\\s*(\\w+)', 1, TE_GlobalStyles['deffunc']),
                    # 'class' followed by an identifier
                    ('\\bclass\\b\\s*(\\w+)', 1, TE_GlobalStyles['defclass']),

                    # Numeric literals
                    ('\\b[+-]?[0-9]+[lL]?\\b', 0, TE_GlobalStyles['numbers']),
                    ('\\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\\b', 0, TE_GlobalStyles['numbers']),
                    ('\\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\\b', 0, TE_GlobalStyles['numbers']),

                    # Double-quoted string, possibly containing escape sequences
                    ('"[^"\\\\]*(\\\\.[^"\\\\]*)*"', 0, TE_GlobalStyles['string']),
                    # Single-quoted string, possibly containing escape sequences
                    ("'[^'\\\\]*(\\\\.[^'\\\\]*)*'", 0, TE_GlobalStyles['string']),

                    # From '#' until a newline
                    ('#[^\\n]*', 0, TE_GlobalStyles['comment']),

                    # From '@' until a newline
                    ('#[^\\n]*', 0, TE_GlobalStyles['meta']),
                ]

                # Build a QRegExp for each pattern
                self.rules = [(QtCore.QRegExp(pat), index, fmt) for (pat, index, fmt) in rules]

    
    def highlightBlock(self, text):
        self.tripleQuotesWithinStrings = []
        # Do other syntax formatting
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)
            if index >= 0:
                # if there is a string we check
                # if there are some triple quotes within the string
                # they will be ignored if they are matched again
                if expression.pattern() in ['"[^"\\\\]*(\\\\.[^"\\\\]*)*"', "'[^'\\\\]*(\\\\.[^'\\\\]*)*'"]:
                    innerIndex = self.tri_single[0].indexIn(text, index + 1)
                    if innerIndex == -1:
                        innerIndex = self.tri_double[0].indexIn(text, index + 1)

                    if innerIndex != -1:
                        tripleQuoteIndexes = range(innerIndex, innerIndex + 3)
                        self.tripleQuotesWithinStrings.extend(tripleQuoteIndexes)

            while index >= 0:
                # skipping triple quotes within strings
                if index in self.tripleQuotesWithinStrings:
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
        # If inside triple-single quotes, start at 0
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        # Otherwise, look for the delimiter on this line
        else:
            start = delimiter.indexIn(text)
            # skipping triple quotes within strings
            if start in self.tripleQuotesWithinStrings:
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
    
    """
    def highlightBlock(self, text):
        # Do other syntax formatting
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)

            while index >= 0:
                # We actually want the index of the nth match
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        # Do multi-line strings
        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)

    def match_multiline(self, text, delimiter, in_state, style):
        # If inside triple-single quotes, start at 0
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        # Otherwise, look for the delimiter on this line
        else:
            start = delimiter.indexIn(text)
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
    """
