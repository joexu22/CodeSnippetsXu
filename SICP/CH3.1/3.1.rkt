#lang racket
(require rackunit)

(define (make-accumulator base-number)
	(define (procedure added-value)
		(set! base-number (+ base-number added-value))
		base-number)
	procedure)

(define A (make-accumulator 5))
(check-equal? (A 10) 15 "Accumulate 10 onto 5")
(check-equal? (A 10) 25 "Accumulate 10 onto 15")

(define B (make-accumulator 0))
(check-not-equal? (B 12) 13 "Should not be 13")