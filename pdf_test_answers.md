# 1 Python
## Mutable / Imutable types
### Vyjmenuj alespoň tři “proměnlivé” (mutable) a “nezměnitelné” (immutable) vestavěné (built-in) typy 
**Mutable** - můžeme je změnit, po vytvoření:
* List, Dictionary, Set

**Imutable**:
* Tuple, Bytes, Float

### Jaký je rozdíl mezi list a tuple? 
U tuple se používájí jednoduché závorky `()`, u listu máme hranaté `[]`.
Tuple nemůžeme po vytvoření upravit, tj měnit hodnoty v jednotlivých polích, ideálně pokud si načteme data, které se nesmí změnit v průběhu programu. U listu můžeme hodnoty doplňovat a měnit i po vytvoření.

### Co se stane, pokud předáte argument do funkce a uvnitř ho změníte? Změní se hodnota tohoto argumentu po zavolání dané funkce? (viz druhý příklad v sekci Code Snippets.)
List 1 a 3 odkazují na stejný list, tj. při použití metody oba rozšíří stejný list. List 2 si vytváří vlastní. Pokud použijeme `id()` uvidíme že list1 a list3 sdílí stejný pamětový prostor (odkazují na stejný objekt):
```
print(id(list1)) -> 2651486529344
print(id(list2)) -> 2651486515136
print(id(list3)) -> 2651486529344

```
## Shallow / Deep Copy
### Jaký je rozdíl mezi shallow a deep kopií v Pythone?
Shallow metoda vytvoří pouze kopii objektu, ale nevytvoří kopii objektů, které obsahuje, např list (vnitřní) v listu. Pokud budeme měnit vnitřní list, změna bude platná jak pro originál tak i pro shallow kopii.
Deep kopie vytvoří kopii i vnitřních objektů.
## Concurrent Computation in Python 
## Jaké možnosti nabízí Python pro implementování konkurentních výpočtů? Stručně je popište.
**Threading** - umožňuje pracovat s vlákny, sdílející stejný paměťový prostor, což znamená, že jsou vhodná pro úlohy spojené s I/O

**Multiprocessing** - poskytuje způsob práce s procesy. Proces má svůj vlastní paměťový prostor a běží nezávisle, což umožňuje lepší pararelní běh na vícejádrových CPU. Na rozdíl od vláken mohou procesy v modulu multiprocessing plně využívat více jader.

**Asyncio** - zavádí asynchronní programování pomocí corutin a událostní smyček. Je zvláště vhodný neblokujících operací (I/O sítťové aplikace). Dokáže zpracovávat více úloh současně v rámci jednoho vlákna a efektivně využívat zdroje.

## Design Patterns, Python Idioms, and OOP
### Stručně popište návrhový vzor *singleton*. Uveďte alespoň 1 příklad praktického využití. 
Umožňuje vytvořit pouze jednu instanci třídy po celou dobu životnosti programu. Použití singletonva patternu má několik výhod. Pokud chceme omezit přístup ke sdílenému prostředku. Chceme-li vytvořit globální místo přístupu. Popřípadě vytvořit pouze jednu instanci třídy po celou dobu životnosti programu. Jako příklad by mohl sloužit: správce připojení k databázi.

### Jak by jste implementovali *iterator* třídu (class)? Co by měla obsahovat (například jaké metody)? 
Jsou potřeba dvě metody a to `__iter__()`, která vrací celkový objekt a metoda `__next__()`, která vrací další hodnotu ze sekvence.

### Co to je *monkey patching*? 
Je to část kódu Pythonu, která za běhu rozšiřuje nebo upravuje jiný kód. Např. u unit testu nahrazení metody, která se připojuje do databáze (externě), jednoduchou funkci, která vráti pevná data.

### Co to je dependency injection a jak byste ji implementovali?
Zaměřuje se na dosažení volné vazby mezi objekty nebo třídami. Jde o to aby třídy měly objekty přímo hotové a sami si je nevytvářely.
Bez použiti DI, by jsme vytvořili objekt přímo v init metodě:
```
    def __init__(self) -> None:
        self.other_class = Slave()
```
Pokud použijeme DI, tak objekt už je vytvořen mimo a je už vložen v parametrech:
```   
    def __init__(self, slave: Slave) -> None:
        self.other_class = slave
```

### Jaký je rozdíl mezi *instanční*, *statickou* a *třídní* metodou? 
**Instační** metoda:
* Definováno pomocí klíčového slova def v rámci třídy.
* Vždycky obsahuje první parametr představující instanci třídy většinou označen jako **self** a tím automaticky předá instanci
* Může přistupovat a upravovat atributy instance a volat jiné metody instance.
* Obecně se používá pro operace, které zahrnují data konkrétní instance.

**Třídní** metoda:
* Definováno pomocí dekorátoru __@classmethod__ nad definicí metody.
* Vezměte **cls** jako první parametr, který představuje samotnou třídu (podobně jako self pro instance).
* Může přistupovat a upravovat atributy na úrovni třídy a volat další metody třídy.
* Užitečné pro operace, které se týkají třídy jako celku, nikoli konkrétní instance.

**Statická** metoda:
* Definováno pomocí dekorátoru __@staticmethod__ nad definicí metody.
* Neberte žádný speciální první parametr (žádné __self__ nebo __cls__).
* Nelze přistupovat nebo upravovat atributy instance nebo třídy přímo.
* Používá se pro operace, které souvisejí s třídou, ale nevyžadují přístup k datům konkrétní instance nebo třídy.

### Co jsou to dunder/magické metody? Vyjmenujte a stručně popište pár z nich.
Metody, které mají před a za názvem dvojité podržítko např. `__str__(self)`. Tyto metody poskytují způsob, jak definovat chování pro vestavěné operace a syntaktické konstrukce, jako jsou aritmetické operace, porovnávání, reprezentace řetězců a další.

**Pár typů**
* `__add__()` - definuje co se má stát při sčítání dvou objektů stejné třídy
* `__str__()` - metoda vrací reprezentace objektu jako string
* `__new__()` - vytvoří nový objekt třídy
* `__init__()` - zodpovědná za inicializaci instance po jejím vytvoření

### Co jsou a jak byste implementovali privátní, chráněné, a veřejné atributy třídy v Pythonu? Co jejich použití znamená pro třídní dědičnost?
* **public**(veřejné) atributy jsou přístupné odkudkoli, uvnitř i vně třídy.
* **protected** (chráněné) atributy třídy jsou přístupné ve třídě a jsou také k dispozici jejím podtřídám. Žádnému jinému prostředí není povolen přístup (jde o konvenci, není jak např. v Javě omezeno). To umožňuje, aby konkrétní prostředky nadřazené třídy byly zděděny podřízenou třídou. Používá se před názvem jednoduché podtržítko.
* **private** (privátní) omezuje přístup k jakékoli proměnné instance mimo třídu. Předřazení názvu proměnné dvojitým podtržítkem, aby se specifikovalo chráněného a soukromého přístupu. Při použití mimo třídu vyvolá _Atribute error_

### Co jsou to context managers a jak byste je použili?
Poskytují pohodlný způsob správy zdrojů (manipulace se soubory, síťová a databázová připojení). Používají se příkazem `with`. Primární výhodou použití kontextových manažerů je, že zaručují správné nastavení, i když je během provádění bloku kódu vyvolána výjimka (exception).

### Kdy byste implementovali vlastní výjimku? 
Když chceme definovat konkrétní chybové stavy, které jsou jedinečné pro naši aplikaci/modul.

### Co jsou to dekorátory? Vymenujte alespoň jeden příklad jejich použití. Je možné aplikovat více dekorátorů najednou? 
Flexibilní způsob, jak upravit nebo rozšířit chování funkcí nebo metod beze změny jejich kódu. Dekorátory umožňují zabalit funkci do jiné funkce, často přidávají procesy (např.protokolování/ověřování) před nebo za dekorovanou funkci. Jelikož wrapper rozšiřuje funkci, tak můžeme stohovat (stack) decorátory nad sebe.

## Code Snippets
### Co by mělo být výstupem následujících ukazek kódu? 
Kód:
```
print([1, 2, 3][10:])
print(r" ict a\nd media ")
```
Výstup:
```
[]
 ict a\nd media
```
Kód:
```
def extendlist(val, list=[]):
    list.append(val)
    return list


list1 = extendlist(42)
list2 = extendlist(42, [])
list3 = extendlist("item")
print(list1)
print(list2)
print(list3)
```
Výstup:
```
[42, 'item']
[42]
[42, 'item']
```
### Implementujte funkci, která najde všechny lichá čísla v intervalu <1; 100 000> a uloží je jako list. 
```
def odd_numbers(start=1, end=100000) -> list:
    return [odd for odd in range(start, end + 1, 2)]
```
### Implementujte funkci, která generuje nekonečnou řadu lichých čísel.
```
def odd_numbers():
    n = 1
    while True:
        n += 2
        # print(n) ?     
```
Jedná se o upravený iterátor `count()`
### Napište regulární výraz, který nalezne protokol, IPv4 adresu a port z řetězce níže. Na vstupu se může vyskytnout libovolný protokol, IPv4 adresa a libovolný port. Protokol a port jsou volitelné části a nemusí se vyskytnout. V řetězci níže musí regulární výraz najít skupiny “protocol=udp”, “ipv4=127.0.0.1”, “port=53”: 
`r"(?:(?P<protocol>\w+)://)?(?P<ipv4>\d+(?:\.\d+){3})(?:\:(?P<port>\d+))?"`
# 2 Testing and Code Quality
### Jaký je rozdíl mezi jednotkovým a integračním testováním?
**Unit** (jednotkové) test ověřuje, zda každá jednotka – nebo izolovaná část kódu – funguje tak, jak vývojář zamýšlel. Provádějí individuálně. Často se jim říká „testovací případy“ skládající se ze segmentů kódu, které spolupracují při provádění konkrétní funkce. Každý test jednotky vyhodnocuje zapsaný kód, aby bylo zajištěno, že je v souladu s každou konkrétní funkcí.

**Integration** testování je v podstatě test modulu. Zahrnuje moduly, které jsou logicky integrovány, a tyto moduly jsou testovány jako skupina. Konkrétně zaměřuje na datovou komunikaci. Integrační testy jsou kritické vzhledem k tomu, že každý softwarový projekt se obvykle skládá z několika modulů, které jsou kódovány jednotlivými programátory.

### Co je to mocking a jaké má beneﬁty při testování?
Je technika používaná při testování softwaru k vytvoření simulovaných verzí komponent nebo závislostí, se kterými interaguje testovaná jednotka kódu. Mocking umožňuje izolovat testovanou jednotku od jejích závislostí, což zajišťuje, že se test soustředí pouze na chování samotné jednotky bez zapojení skutečných externích komponent.

**Benefity:**
* Kontrolované chování - je možné simulovat různé druhy možností
* Rychlost a účinost - není potřeba externích zdrojů
* Opakovatelné testy
* Redukuje komplexnost
* Paralelní testování

### Co to je white box a black box testování? 
**White box**

Zaměřuje se na vnitřní logiku a strukturu testovaného softwaru. Testeři mají přístup k internímu kódu, datovým strukturám, algoritmům a detailům implementace. Cílem je zajistit, aby kód fungoval správně, dodržoval specifikace návrhu a spouštěl všechny cesty a podmínky.

**+** Efektivní při identifikaci logických chyb, zranitelnosti kódu a odhalování skrytých chyb v kódu. 

**-** Vyžaduje znalost vnitřností kódu, nemusí zachytit problémy na úrovni systému nebo s integrací.

**Black box**

Zaměřuje se na vnější chování softwaru bez ohledu na jeho vnitřní strukturu. Interagují se softwarem jako koncový uživatel. Cílem je ověřit, zda software splňuje funkční požadavky, specifikace a očekávání uživatelů.

**+** Napodobuje interakce uživatelů v reálném světě, identifikuje problémy z pohledu uživatele a nespoléhá se na znalost kódu.

**-** Může přehlédnout určité logické chyby nebo zranitelnosti skryté v kódu.

### Co to je statická analýza kódu (nápověda: pep8)?
Statické analýza identifikuje potenciální problémy, chyby, zranitelnosti a dodržování standardů kódování zkoumáním struktury, syntaxe a sémantiky kódu.

### Co znamenají zkratky CI a CD? 
Continuous integration (CI) je postup automatizace integrace změn kódu od více přispěvatelů do jediného softwarového projektu. Vývojářům umožňuje často slučovat změny kódu do centrálního úložiště, kde se pak spouštějí buildy a testy.

Continuous delivery (CD) je automatické doručování dokončeného kódu do prostředí.

# 3 DATABASE

### Jaké jsou rozdíly mezi SQL a NoSQL databázovými systémy?
Databázový systém SQL(MySQL, PostgreSQL, Oracle, Sqlite) používá k reprezentaci dat a jejich vztahů tabulkový relační model. NoSQL (MongoDB, BigTable, Redis, RavenDB) databáze poskytuje mechanismus pro ukládání a získávání dat jiných než tabulkových modelů používaný v relačních databázích.

### Co je to databázový index? Jaké typy indexů znáte? (Ideálně v PostgreSQL) 
Indexy jsou běžným způsobem zvýšení výkonu databáze. Index umožňuje databázovému serveru najít a načíst konkrétní řádky mnohem rychleji, než by tomu bylo bez indexu. B-Tree

### Co byste dělali, když byste měli optimalizovat nějaký SQL dotaz? 
* Místo * specifikovat pouze sploupce, které potřebuji.
* Vyhnout se používání výrazu __or__
* Doplnit indexy, zkontrolovat nepoužíváné
* Použití **TOP** pro dotazování vzorků
* Vyvarovat se řetezení __JOIN__

### Co to je ELT a ETL (nápověda: extrakce, načítání, transformace)? Jaké jsou mezi nimi rozdíly? 
ETL (Extract, Transform, Load) a ELT (Extract, Load, Transform) jsou dva různé procesy integrace dat. ETL i ELT zahrnují přesun a zpracování dat ze zdrojových systémů do cílového úložiště, liší se však posloupností kroků a přístupem k transformaci dat.
* ETL zahrnuje transformaci dat na samostatném serveru pro zpracování před jejich přenosem do datového uložiště.
* ELT provádí transformace dat přímo v rámci samotného datového uložiště. Na rozdíl od ETL umožňuje ELT odesílání nezpracovaných dat přímo do do datového uložiště, což eliminuje potřebu fázování procesů.
