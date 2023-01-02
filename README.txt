# ALD_Sem
Program je kódovaný v Pythonu. Zdrojový kód je ve složce ALD_Sem v souboru ALD_Sem.py.
V této složce je i složka images, která obsahuje sadu obrázků pro vytváření herního světa.

Na devátém řádků jsou proměnné x a y, které zadávají počet řádků a sloupců herního světa.
Program funguje jak pro čtvercové světy, tak i pro obdelníkové.
Rozměry kanvasu jsou vypočítané od rozměrů světa (násobím počet řádků/sloupců 45, protože obrázky mají rozměr 45x45 pixelů)

Dále se dá manipulovat se šancí na výskyt určitých obrázků (řádek 61-69, případně řádek 27 pro metodu Choose4())
Při volání metody výběru je vždy zadáno číslo obrázku a poté jeho šance na výskyt v procentech (maximum dohromady by tedo mělo být 100, minimum 1).

Čísla/jména obrázků jsou neměnná, jelikož je na jejich jménech a uspořádání postavena logika vytváření světa.

Logika se skládá ze dvou if statementů. První z nich kontroluje jestli pole nad ním je obsazeno obrázkém, který navazuje směrem dolů (např. obrázek 1).
Druhý kontroluje jestli pole na levo od něj je obsazeno obrázkém, který navazuje směrem vpravo (např. obrázek 10).
Dále následuje výběr jednoho ze čtyř možných obrázků. Ten je určený výsledkem těchto dvou if statementů.
Takto funguje generace světa pro všechny pole, která nejsou v prvním řádku nebo sloupci.
Pro pole v prvním sloupci je uplatněn pouze první if statement, pro pole v prvním řádku pouze druhý if statement.
Levý horní roh světa (pole [0,0]) je určen zcela náhodně.

Kód případně obsahuje krátké komentáře v angličtině k jednotlivým metodám.
