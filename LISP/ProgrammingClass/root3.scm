(define (root3-iter guess x)
    (if (good-enough? guess x)
    guess
    (root3-iter (improve guess x) x)))

(define (improve guess x)
    (average guess (/ x guess)))

(define (average x y)
    (/ (+ x y) 3.0))

(define (good-enough? guess x)
    (< (abs ( - (cube guess) x)) 0.001))

(define (cube x)
    (* x x x))

(define (square x)
    (* x x))

(define (root3 x)
    (root3-iter 1.0 x))

(define (sqrt2 x)
    (sqrt-iter 1.0 x))

(inspect (root3 2))
