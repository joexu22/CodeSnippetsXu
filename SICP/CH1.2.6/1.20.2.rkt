#lang racket
(require rackunit)

(define (square x) (* x x))

(define (expmod base exp m)
	(cond
		((= exp 0) 1)
		((even? exp)
			(remainder
				(square (expmod base (/ exp 2) m))
				m))
		(else
			(remainder
				(* base (expmod base (- exp 1) m))
				m))))

(define (fermat-test n)
	(define (try-it a)
		(= (expmod a n n) a))
	(try-it (+ 1 (random(- n 1)))))

(define (fast-prime? n times)
	(cond
		((= times 0) true)
		((fermat-test n) (fast-prime? n (- times 1)))
		(else false)))

(check-equal? (expmod  2 7 5) 3 "128 % 5 = 3")
(check-equal? (expmod  12 0 24) 1 "1 % 24 = 1")
(check-true (fermat-test 7) "7 is a prime") ;;; it'll always pass
(check-true (fast-prime? 7 3) "7 is a prime") ;;; it'll always pass
(check-false (fast-prime? 21 5) "21 is not a prime") ;;; this has probability to fail

;;; Carmichael Number (I've Been Fooled)
;;; (check-false (fast-prime? 561 10) "561 is not a prime") ;;; this often fails despite 3*187=561
;;; (check-false (fast-prime? 561 1000000) "561 is not a prime") ;;; this often fails despite 3*187=561