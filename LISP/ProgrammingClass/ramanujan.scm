;{
(define (cont-frac n x)
    (define (recur i)
        (if (> i n)
            0.0
            (^ (+ 1 (* (+ x i) (recur (+ i 1)))) .5)
        )
    )
    (recur 0)
)

(define (ramanujan n x)
    (if (= n 0) 
        0.0
        (cont-frac n x)
    )
)
;}

(define (ramanujan n x)
    (define (recur i)
        (if (> i n)
            0.0 
            (^ (+ 1 (* (+ x i) (recur (+ i 1)))) .5)
        )
    )
    (if (= n 0) 
        0.0
        (recur 0)
    )
)

(define (iramanujan n x)
    (define (iter-r i result)
        (if (= i 0) 
            result
            (iter-r (- i 1)
                (^ (+ 1 (* (- (+ x i) 1) result)) .5)
            )
        )
    )
    (if (= n 0)
        0.0
        (iter-r n 1)
    )
)       

(inspect (^ (+ 1 (* (- (+ 3 1) 1) 4)) .5))

(println "the value of is \"x + 1\"")

(inspect (ramanujan 0 3))
(inspect (ramanujan 1 3))
(inspect (ramanujan 2 3))
(inspect (ramanujan 3 3))
(inspect (ramanujan 4 3))
(inspect (ramanujan 5 3))
(inspect (ramanujan 115 3))
(inspect (ramanujan 115 4))
(inspect (ramanujan 115 5))
(inspect (ramanujan 115 2))
(inspect (iramanujan 0 3))
(inspect (iramanujan 1 3))
(inspect (iramanujan 2 3))
(inspect (iramanujan 3 3))
(inspect (iramanujan 4 3))
(inspect (iramanujan 5 3))
(inspect (iramanujan 10 3))
(inspect (iramanujan 20 3))
(inspect (iramanujan 40 3))
(inspect (iramanujan 80 3))
(inspect (iramanujan 100 3))
