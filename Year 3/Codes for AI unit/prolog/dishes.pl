in(p0,kitchen).
in(c1,diningroom).
in(c2,kitchen).
in(c3,kitchen).
in(c4,kitchen).
plate(p0).
cup(c1).
cup(c2).
cup(c3).
cup(c4).
clean(p0).
dirty(c1).
clean(c2).
dirty(c3).
clean(c4).

toWash(X):-in(X,kitchen),format("~n In:~w",[X]),
    cup(X),format("~n Cup:~w",[X]),!,
    dirty(X),format("~n Dirty:~w",[X]),
    fail.
