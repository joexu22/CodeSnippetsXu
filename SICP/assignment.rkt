#lang racket
(sqrt 100)
(identity 100)

; uses set!
(define (make-accumulator initial_number)
	(lambda (x) (set! initial_number (+ initial_number x)) initial_number))

(define A (make-accumulator 0))
(A 1)
(A 1)
