/*
  ---------Lab Exercise 4-------
  Name: Cyrus David G. Pastelero
  Subject: Programming Paradigms
  Section: A
  Date: Oct 13, 2020
  ------------------------------
*/

% All Females database 1
female(missScarlet).
female(mrsWhite).
female(mrsPeacock).
female(drOrchid).

% All Males database 2
male(profPlum).
male(colonelMustard).
male(revGreen).

% -----Person X hates Y----------

% database 3
hates(missScarlet, revGreen).

% database 4
hates(revGreen, missScarlet).

% database 5
hates(profPlum, mrsWhite).
hates(mrsWhite, profPlum).

% database 6
hates(colonelMustard, Y) :- female(Y).
hates(colonelMustard, profPlum).


% -----Person X likes Y-----------

% database 7
likes(missScarlet, drOrchid).
likes(mrsPeacock, drOrchid).

% database 8
likes(drOrchid, mrsPeacock).

% database 9
likes(missScarlet, mrsWhite).

% database 10
likes(missScarlet, profPlum).
likes(profPlum, missScarlet).

% database 11
likes(profPlum, X) :- hates(colonelMustard, X).


% ---Enemies if person X hates Y or person Y hates X---

% database 12
enemies(X, Y) :- hates(X, Y), hates(Y, X).

% ---Friends if person X likes Y or person Y likes X---
% ---Or Person Y is enemies with Person Xs Enemy---

% database 13
friends(X, Y) :- likes(X, Y), likes(Y, X).

% database 14
friends(X, Y) :- enemies(X, Z), enemies(Z, Y).
