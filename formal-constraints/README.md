# Answer Set Programming for Automated Verification of Intent Consistency
_Brian Muhia, August 2023_

The causal influence diagrams introduced [here](https://docs.google.com/document/d/160Yw_iuvztB6CTT9Osj5wC0sOrEKjfaGkkeeYuwQf4Y/edit?usp=sharing), and the accompanied
reasoning that favours certain diagrams over others based on links to
the "I" node, are simple enough that we can devise automated rules that
check if a diagram is correct or wrong. We call this property "intent
consistency". Here we introduce three simple rules written in the
Answer-Set Programming (ASP) formalism that 

1. find paths between any two nodes X and Y, then check if
1. a path exists from the input node "I" to any decision node, and 
1. fails if there is no direct link from the node "I" to any decision node. 

These rules encode our expectations and intuitions, and let us describe
a framework for automatically deciding if a diagram satisfies them. We
call these rules "intent consistency models" (ICM), after
[https://doi.org/10.1017/S1471068410000554].


```
% ...after encoding the CID using ASP facts link(), decision() and utility(),
% Recursive rule to find a path from X to Y
path(X, Y) :- link(X, Y).
path(X, Y) :- link(X, Z), path(Z, Y).

% Rule that fails if there is no direct link from I or C to any of the decision nodes.
direct_link(I, D) :- link(I, D), decision(D).
:- decision(D), not direct_link("I", D).
:- decision(D), not direct_link("C", D).

% Checks if a path exists from I to any decision node
check(Node) :- decision(Node), path("I", Node).

#show direct_link/2.
#show check/1.
```

ASP enables us to encode the graphs described here using facts, and run
them through a conventional SAT solver like 'clingo' that checks for
satisfiability. We can then describe unsatisfiable graphs as "incorrect".
