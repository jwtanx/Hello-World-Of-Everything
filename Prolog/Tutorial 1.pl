% Stopping the prolog
| ?- halt

% Starting the prolog
| ?- gprolog

% To start your prolog
| ?- [scriptName].

% Another way to load the prolog
| ?- consult('scriptName.pl').

% To show all the information about your prolog
| ?- Listing.

% To show part the information about your prolog
| ?- listing.

/* First script */
| ?- write('Hello World'), nl, write('Let\'s see this second new line with the \'nl\' keyword').


/****************************************************/

% Script Name: couple.pl
/* Facts */
% romeo loves juliet
loves(romeo, juliet).

/* Rules */
% juliet loves romeo if romeo loves juliet
loves(juliet, romeo) :- loves(romeo, juliet).

>> Load the script to check whether juliet loves romeo
| ?- [couple].
yes
| ?- loves(juliet, romeo).
yes

% Check who loves juliet, the 'X' must be capitalised
| ?- loves(romeo, X).
X = juliet 

/****************************************************/

% Script Name: gender.pl
/* Facts */
male(ali).
male(abu).
male('ah kau').

female(sarah).
female(siti).

>> Load
| ?- listing(male).
ali
abu
ah kau

| ?- male(X), female(Y).
X = ali
Y = sarah ? ; <--- Hit semicolon to go to the next one

X = abu
Y = siti ? ;

X = 'ah kau'
Y = sarah % NOTE THAT THE SARAH IS LOOP BACK

/****************************************************/

% cook.pl
/* Facts */
got(dough).
got(cheese).
got(sauce).
with_gordonramsay(littlejack).

/* Rules */
bake(pizza) :- 
    got(dough),
    got(cheese),
    got(sauce),
    with_gordonramsay(littlejack).

does_jack_bake_pizza :- bake(pizza),
    write('Little Jack bakes pizza with Gordon Ramsay')

>> Load
| ?- bake(pizza).
yes

| ?- does_jack_bake_pizza.
'Little Jack bakes pizza with Gordon Ramsay'
yes

/****************************************************/

% parents.pl
/* Facts */
parent(john, albert).
parent(albert, sarah).
dance(sarah).

/* Rules */
get_grandfather :-
    parent(Y, sarah),
    parent(X, Y),
    write('Sarah grandfather is '),
    write(X), nl.

get_grandfather_format :-
    parent(Y, sarah),
    parent(X, Y),
    format('~w is ~s\'s ~s ~n', [X, 'sarah', 'grandfather']).
    % '~w'(word), '~s'(string), '~n'(nextline).

% Check who is the child of albert and also dances
| ?- parent(albert, X), dance(X).
sarah

| ?- parent(Y, sarah), parent(X, Y).

X = john
Y = albert ;

| ?- get_grandfather.
sarah grandfather is john

| ?- get_grandfather_format.
john is sarahs grandfather

/****************************************************/
% Annonymous variable %

% catpeeonbed.pl
/* Facts */
% tabby pee on bed
pee(tabby, bed).

/* Rules */
hates(romeo, X) :- pee(X, bed).

| ?- hates(romeo, Y).
Y = tabby

| ?- hates(X, Y).
X = romeo
Y = tabby

/****************************************************/
Operator

% grade.pl
my_grade(5) :- write('Kindergarden').
my_grade(6) :- write('Go to 1st grade').
my_grade(Age) :- 
    Grade is Age - 5,
    format('Go to grade ~w', [Grade]).

/****************************************************/
facts in a fact

% pet.pl
owns(romeo, pet(cat, tabby)).
owns(romeo, pet(dog, lucky)).

| ?- owns(romeo, pet(Type, _)).
Type = cat ;
Type = dog ;

/****************************************************/
More formatting

% customer.pl
customer(sally, smith, 123.3).
customer(john, cena, 10.266).

get_cust_bal(Fname, Lname) :-
    customer(Fname, Lname, Bal),
    write(Fname), tab(1),
    format('~w owes us $~2f ~n', [Fname, Bal]).


| ?- get_cust_bal(john, _)
john cena owes us $10.27

/****************************************************/
Conditional checking

% vertical line or horizontal line
vertical(line(X, Y), line(X, Y2)).
horizontal(line(X, Y), line(X2, Y)).

| ?- vertical(line(5, 10), line(5, 20)).
Yes

/****************************************************/
Boolean

| ?- alice = alice.
Yes

| ?- 'alice' = alice.
Yes

% Not equal sign
| ?- \+ (alice = albert).
Yes

% Operator :: Less than or equal
| ?- 3 =< 15.
Yes

% Operator :: More than or equal
| ?- 3 >= 15.
No

rich(moeny, X) = rich(Y, no_debt).
X = no_debt
Y = money

/****************************************************/
% Trace

% start
| ?- trace.
| ?- human(ali).

% stop
| ?- notrace.

/****************************************************/
Number

| ?- X is 3 + (20 * 2).
X = 43

| ?- \+(3 = 10).

% equality
| ?- 5+2 =:= 2+5.
Yes

| ?- 5+4 =\= 5+2.
Yes

% Or Operator
| ?- 5 > 10 ; 10 > 1.
Yes

% And Operator
| ?- 5 > 1 , 10 > 1.
Yes

% Mod
| ?- X is mod(7, 2).
X = 1

/****************************************************/
Function
double(X, Y) :-
    Y is X*2.

| ?- double(10, Y).
Y = 20

/****************************************************/
Random
| ?- random(0, 10, X). % 0 to 9 only will be generated
X = 9

/****************************************************/
Between
| ?- between(0, 10, X).
X = 0 ? ;
X = 1 ? ;
X = 2 ? ;
X = 3 ? ;
X = 4 ? ;
X = 5 ? ;
X = 6 ? ;
X = 7 ? ;
X = 8 ? ;
X = 9 ? ;
X = 10 ?

/****************************************************/
Successor
| ?- succ(4, X).
X = 5

/****************************************************/
Absolute value
| ?- X is abs(-5).
X = 5

| ?- abs(-5, X).
X = 5

/****************************************************/
Max and Min
| ?- X is max(10, 100).
X = 100

| ?- X is min(10, 100).
X = 10

/****************************************************/
Round
| ?- X is round(10.45).
X = 10

| ?- X is round(10.55).
X = 11

/****************************************************/
Truncate & floor & ceiling
| ?- X is truncate(10.56).
X = 10

| ?- X is floor(10.67).
X = 10

| ?- X is ceiling(10.23)
X = 11

/****************************************************/
Power
| ?- X is 2**3
X = 8.0

/****************************************************/
Even
is_even(X) :-
    Y is X//2, X =:= Y*2.

/****************************************************/
Math
/*
sqrt, sin, cos, tan, asin, acos, atan, tan2, sinh, asinh, acosh, atanh, log, log10, exp, pi, e
*/

Continue: https://youtu.be/SykxWpFwMGs?t=2659

