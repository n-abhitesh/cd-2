%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s);
%}

%union {
    int dval;
}

%token <dval> DIGIT
%type <dval> expr expr1

%%

line : expr '\n' { printf("%d\n", $1); }
     ;

expr : expr '+' expr1 { $$ = $1 + $3; }
     | expr '-' expr1 { $$ = $1 - $3; }
     | expr '*' expr1 { $$ = $1 * $3; }
     | expr '/' expr1 { $$ = $1 / $3; }
     | expr1
     ;

expr1 : '(' expr ')' { $$ = $2; }
      | DIGIT           { $$ = $1; }
      ;

%%

int main() {
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    printf("%s\n", s);
}
