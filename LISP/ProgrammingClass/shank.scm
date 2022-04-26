(define (w f i)
    (cond
        ((= i 0) (f i))
        (else (Shank f i))
    )
)

(define (Shank f i)
    (define A (S f (+ i 1)))
    (define B (S f (- i 1)))
    (define C (S f i))
    (/ (- (* A B) (* C C)) (- (+ A B) (* 2.0 C)))
)

(define (S f n)
    (sum f 0 inc n)
)

;{
(define (sum-cube a b)
    (sum cube a inc b))

(define (rand-sum a b f)
    (sum f a inc b))

(inspect (sum-cube 1 10))
(inspect (rand-sum 1 10 (lambda (x) (* x x x))))

(define (S f n)
    (define (iter-S count amount)
        (if (> count n)
            amount
            (iter-S (+ count 1) (+ f amount))
        )
    (iter-S 0 0)
)

((lambda (f) (f f 1 0))
    (lambda (f n acc)
    (if (> n 10)
        acc
        (f f (+ n 1) (+ acc n)))))


;}

(define (sum term a next b)
    (if (> a b)
        0
        (+ (term a) (sum term (next a) next b))
    )
)

(define (inc n) (+ n 1))

(define (cube x) (* x x x))

(define (sum-cube a b)
    (sum cube a inc b))

(define (rand-sum a b f)
    (sum f a inc b))

(inspect (sum-cube 1 10))
(inspect (rand-sum 1 10 (lambda (x) (* x x x))))
(inspect (S (lambda (x) (+ x 2)) 5))
(inspect (w (lambda (x) (+ x 2)) 7))
(inspect (w (lambda (x) (+ (** x 2) 1)) 1))
(inspect (w (lambda (x) (+ (** x 2) 5)) 2))
(inspect (w (lambda (x) (+ x 2)) 7))
