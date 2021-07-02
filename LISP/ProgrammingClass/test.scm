(define x 2)
(define a (readInt))
(inspect (if (= a 0) x (/ a x)))
(inspect (my-if (= a 0) x (/ a x)))

(define (my-if a b c)
    (if (true? a)
        b
        c
        )
    )
