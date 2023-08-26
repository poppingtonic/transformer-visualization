%*
Representing causal influence diagrams for factored cognition using ASP

We encode CIDs as facts and our intuitions about "intent alignment" as constraints
to check the facts against.

pycid.CID(
  [("C", "M1"),
   ("I", "C"),
   ("I", "M1"),
   ("M1", "O")],
  decisions=["M1"],
  utilities=["O"]
)

*%



link("C", "M1").
link("I", "C").
link("I", "M1").
link("M1", "O").

decision("M1").
utility("O").
chance("I";"C").

% Recursive rule to find a path from X to Y
path(X, Y) :- link(X, Y).
path(X, Y) :- link(X, Z), path(Z, Y).

% This rule fails if there is no direct link from I to any of the decision nodes
direct_link(I, D) :- link(I, D), decision(D).
:- decision(D), not direct_link("I", D).


% Query to check if a path exists from I to any decision node
check(Node) :- decision(Node), path("I", Node).


#show direct_link/2.
#show check/1.
