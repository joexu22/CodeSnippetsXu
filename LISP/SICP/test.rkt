#lang racket

;;; if statements
(>= 2 2)

;;; let usage
(let ([x 5]) 5)

;;; chained let useage
(let ([x 5])
	(let ([x 2] [y x])
		(list y x)))

;;; how random works
(random 3)
(random 0 3)

;;; random with ranges
(define (test-random-1-n n)
	(+ 1 (random(- n 1))))

(newline)
(test-random-1-n 2)
(test-random-1-n 2)
(test-random-1-n 2)

;;; timing
(define a 0)
(define b 0)
(set! a (current-inexact-milliseconds))
(set! b (current-inexact-milliseconds))
(- b a)