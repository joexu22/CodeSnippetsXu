(define (egypt* b c)
    (define (iter-up a b c d)
        (cond
            ((> a b) (iter-down a b c d))
            (else (iter-up (+ a a) b (+ c c) d))
        )
    )
    (define (iter-down a b c d)
        (cond
            ((= b 0) d)
            ((<= a b) (iter-down (halve a) (- b a) (halve c) (+ c d)))
            (else (iter-down (halve a) b (halve c) d))
        )
    )
    (iter-up 1 b c 0)
)

(define (halve x)
    (define (iter-half x y z)
        (cond
            ((<= x 1) 0)
            ((< x y) (- z 1))
            (else (iter-half x (+ y 2) (+ z 1)))
        )
    )
    (iter-half x 0 0)
)
    


(inspect (halve 4))
(inspect (halve 8))
(inspect (halve 49))
(inspect (egypt* 10 7))
(inspect (egypt* 77 777))
(inspect (egypt* 56 3))
