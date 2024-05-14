%{
#include "calc.tab.h"
%}

%%

[ \t]+              ; /* skip whitespace */
[0-9]+              { yylval.num = atoi(yytext); return NUM; }
[-+*/\(\)\n]        { return *yytext; }
.                   { fprintf(stderr, "Invalid character: %s\n", yytext); }

%%