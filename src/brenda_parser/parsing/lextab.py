# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('ACCESSION', 'AND', 'CITATION', 'COMMENT', 'CONTENT', 'EC_NUMBER', 'END', 'ENTRY', 'ENZYME_ENTRY', 'HEADER', 'LANGLE', 'LCURLY', 'LPARENS', 'POUND', 'PROTEIN', 'PROTEIN_ENTRY', 'RANGLE', 'RCURLY', 'REFERENCE_ENTRY', 'RPARENS', 'SPECIAL'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive', 'citation': 'exclusive', 'protein': 'exclusive', 'special': 'exclusive', 'comment': 'exclusive', 'enzyme': 'exclusive', 'protentry': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_ANY_newline>\\n+)|(?P<t_brenda_comment>\\*.+\\n)|(?P<t_POUND>[#])|(?P<t_LANGLE><)|(?P<t_LCURLY>{)|(?P<t_LPARENS>\\()|(?P<t_ANY_END>[/]{3}\\n)|(?P<t_ENZYME_ENTRY>ID\\b)|(?P<t_PROTEIN_ENTRY>PR\\b)|(?P<t_REFERENCE_ENTRY>RF\\b)|(?P<t_ENTRY>[A-Z0-9]{2,4}\\b)|(?P<t_HEADER>[A-Z0-9_]{4,}\\n)|(?P<t_CONTENT>[^\\{\\}\\(\\)\\<\\>\\# \t\r\x0c\x0b\n]+)', [None, ('t_ANY_newline', 'newline'), ('t_brenda_comment', 'brenda_comment'), ('t_POUND', 'POUND'), ('t_LANGLE', 'LANGLE'), ('t_LCURLY', 'LCURLY'), ('t_LPARENS', 'LPARENS'), ('t_ANY_END', 'END'), ('t_ENZYME_ENTRY', 'ENZYME_ENTRY'), ('t_PROTEIN_ENTRY', 'PROTEIN_ENTRY'), ('t_REFERENCE_ENTRY', 'REFERENCE_ENTRY'), ('t_ENTRY', 'ENTRY'), ('t_HEADER', 'HEADER'), (None, 'CONTENT')])], 'citation': [('(?P<t_ANY_newline>\\n+)|(?P<t_citation_CITATION>\\d+)|(?P<t_citation_RANGLE>>)|(?P<t_ANY_END>[/]{3}\\n)', [None, ('t_ANY_newline', 'newline'), ('t_citation_CITATION', 'CITATION'), ('t_citation_RANGLE', 'RANGLE'), ('t_ANY_END', 'END')])], 'protein': [('(?P<t_ANY_newline>\\n+)|(?P<t_protein_PROTEIN>\\d+)|(?P<t_protein_POUND>[#])|(?P<t_ANY_END>[/]{3}\\n)', [None, ('t_ANY_newline', 'newline'), ('t_protein_PROTEIN', 'PROTEIN'), ('t_protein_POUND', 'POUND'), ('t_ANY_END', 'END')])], 'special': [('(?P<t_ANY_newline>\\n+)|(?P<t_special_SPECIAL>[^\\{\\}\\s]+)|(?P<t_special_RCURLY>})|(?P<t_ANY_END>[/]{3}\\n)', [None, ('t_ANY_newline', 'newline'), ('t_special_SPECIAL', 'SPECIAL'), ('t_special_RCURLY', 'RCURLY'), ('t_ANY_END', 'END')])], 'comment': [('(?P<t_ANY_newline>\\n+)|(?P<t_comment_COMMENT>[^\\(\\)\\s]+)|(?P<t_comment_LPARENS>\\()|(?P<t_comment_RPARENS>\\))|(?P<t_ANY_END>[/]{3}\\n)', [None, ('t_ANY_newline', 'newline'), ('t_comment_COMMENT', 'COMMENT'), ('t_comment_LPARENS', 'LPARENS'), ('t_comment_RPARENS', 'RPARENS'), ('t_ANY_END', 'END')])], 'enzyme': [('(?P<t_ANY_newline>\\n+)|(?P<t_ANY_END>[/]{3}\\n)|(?P<t_enzyme_EC_NUMBER>(\\d+)\\.(\\d+)\\.(\\d+)\\.(\\d+))', [None, ('t_ANY_newline', 'newline'), ('t_ANY_END', 'END'), ('t_enzyme_EC_NUMBER', 'EC_NUMBER')])], 'protentry': [('(?P<t_ANY_newline>\\n+)|(?P<t_ANY_END>[/]{3}\\n)|(?P<t_protentry_PROTEIN_ENTRY>PR\\b)|(?P<t_protentry_ENTRY>[A-Z0-9]{2,4}\\b)|(?P<t_protentry_AND>AND)|(?P<t_protentry_ACCESSION>([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\\.\\d+)?)', [None, ('t_ANY_newline', 'newline'), ('t_ANY_END', 'END'), ('t_protentry_PROTEIN_ENTRY', 'PROTEIN_ENTRY'), ('t_protentry_ENTRY', 'ENTRY'), ('t_protentry_AND', 'AND'), ('t_protentry_ACCESSION', 'ACCESSION')]), ('(?P<t_ANY_newline>\\n+)|(?P<t_brenda_comment>\\*.+\\n)|(?P<t_POUND>[#])|(?P<t_LANGLE><)|(?P<t_LCURLY>{)|(?P<t_LPARENS>\\()|(?P<t_ANY_END>[/]{3}\\n)|(?P<t_ENZYME_ENTRY>ID\\b)|(?P<t_PROTEIN_ENTRY>PR\\b)|(?P<t_REFERENCE_ENTRY>RF\\b)|(?P<t_ENTRY>[A-Z0-9]{2,4}\\b)|(?P<t_HEADER>[A-Z0-9_]{4,}\\n)|(?P<t_CONTENT>[^\\{\\}\\(\\)\\<\\>\\# \t\r\x0c\x0b\n]+)', [None, ('t_ANY_newline', 'newline'), ('t_brenda_comment', 'brenda_comment'), ('t_POUND', 'POUND'), ('t_LANGLE', 'LANGLE'), ('t_LCURLY', 'LCURLY'), ('t_LPARENS', 'LPARENS'), ('t_ANY_END', 'END'), ('t_ENZYME_ENTRY', 'ENZYME_ENTRY'), ('t_PROTEIN_ENTRY', 'PROTEIN_ENTRY'), ('t_REFERENCE_ENTRY', 'REFERENCE_ENTRY'), ('t_ENTRY', 'ENTRY'), ('t_HEADER', 'HEADER'), (None, 'CONTENT')])]}
_lexstateignore = {'citation': ' ,\t', 'protein': ' ,\t', 'INITIAL': ' \t\r\x0c\x0b', 'special': ' \t\r\x0c\x0b', 'comment': ' \t\r\x0c\x0b', 'enzyme': ' \t\r\x0c\x0b', 'protentry': ' \t\r\x0c\x0b'}
_lexstateerrorf = {'INITIAL': 't_ANY_error', 'citation': 't_ANY_error', 'protein': 't_ANY_error', 'special': 't_ANY_error', 'comment': 't_ANY_error', 'enzyme': 't_ANY_error', 'protentry': 't_ANY_error'}
_lexstateeoff = {}
