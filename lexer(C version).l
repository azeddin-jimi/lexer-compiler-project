
/*|||Cette partie contient du code C standard. Ici, on inclut la bibliothèque stdio pour utiliser printf.”|||*/

%{
#include <stdio.h>
%}

/*|||À partir d’ici, on définit les règles de reconnaissance des tokens|||*/
%%

"if"        { printf("KEYWORD_IF\n"); }
"while"     { printf("KEYWORD_WHILE\n"); }
"print"     { printf("KEYWORD_PRINT\n"); }

==          { printf("EQUAL\n"); }
=           { printf("ASSIGN\n"); }

[0-9]+      { printf("NUMBER: %s\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]*   { printf("IDENTIFIER: %s\n", yytext); }

\+          { printf("PLUS\n"); }
\-          { printf("MINUS\n"); }
\*          { printf("MULTIPLY\n"); }
\/          { printf("DIVIDE\n"); }

\(          { printf("LPAREN\n"); }
\)          { printf("RPAREN\n"); }

\"([^\"\n])*\"   { printf("STRING: %s\n", yytext); }

[ \t\n]+    { /* ignore */ }

.           { printf("ERROR: %s\n", yytext); }

%%
/*|||“Fin de la section des règles.”|||*/


/*|||“Cette fonction indique la fin de l’analyse du fichier.”|||*/
int yywrap() { return 1; }

int main() {
    printf("=== LEXER START ===\n");

    yylex();  // lancer l'analyse
    printf(" \n");
    printf("=== LEXER END ===\n");    return 0;
}