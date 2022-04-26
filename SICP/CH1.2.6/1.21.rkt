;;; Use the smallest-divisor procedure to find the samllest divisor of each of the following numbers: 199, 1999, 19999

#lang racket
(require rackunit)

(define (smallest-divisor n)
	(define (square x) (* x x))
	(define (find-divisor n i)
		(cond
			((> (square i) n) n)
			((= 0 (modulo n i)) i)
			(else (find-divisor n (+ 1 i)))))
	(find-divisor n 2))

;; output
(smallest-divisor 199)
(smallest-divisor 1999)
(smallest-divisor 19999)

;;; test function
(check-equal? (smallest-divisor 4) 2)
(check-equal? (smallest-divisor 199) 199)
(check-equal? (smallest-divisor 1999) 1999)
(check-equal? (smallest-divisor 19999) 7)
