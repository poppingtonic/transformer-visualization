%*
Checking intent consistency for agent variants 7-PV{1,2}
This program is unsatisfiable for 7-PV1, but satisfiable for 7-PV2.

(7-PV1) Parallel Variant 1 where the user's intent is omitted from the context of agents M2-M6.
variant_1  = pycid.CID(
    [
        ("C", "M1"),
        ("C", "M2"),
        ("C", "M3"),
        ("C", "M4"),
        ("C", "M5"),
        ("C", "M6"),
        ("C", "M7"),
        ("I", "M1"),
        ("I", "M7"),
        ("M1", "M2"),
        ("M1", "M3"),
        ("M1", "M4"),
        ("M1", "M5"),
        ("M1", "M6"),
        ("M2", "M7"),
        ("M3", "M7"),
        ("M4", "M7"),
        ("M5", "M7"),
        ("M6", "M7"),
        ("M7", "O"),
    ],
    decisions=["M1", "M2", "M3", "M4", "M5", "M6", "M7"],
    utilities=["O"]
)
variant_1.draw()

*%

link("C", "M1").
link("C", "M2").
link("C", "M3").
link("C", "M4").
link("C", "M5").
link("C", "M6").
link("C", "M7").
link("I", "M1").
link("I", "M7").
link("M1", "M2").
link("M1", "M3").
link("M1", "M4").
link("M1", "M5").
link("M1", "M6").
link("M2", "M7").
link("M3", "M7").
link("M4", "M7").
link("M5", "M7").
link("M6", "M7").
link("M7", "O").

decision("M1";"M2";"M3";"M4";"M5";"M6";"M7").
utility("O").

% Recursive rule to find a path from X to Y
path(X, Y) :- link(X, Y).
path(X, Y) :- link(X, Z), path(Z, Y).

% Rule that fails if there is no direct link from I to any of the decision nodes.
direct_link(I, D) :- link(I, D), decision(D).
:- decision(D), not direct_link("I", D).

% Checks if a path exists from I to any decision node
check(Node) :- decision(Node), path("I", Node).

#show direct_link/2.
#show check/1.
