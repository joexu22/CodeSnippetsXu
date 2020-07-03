#lang racket
(require rackunit)

(define (prime? n)
	(= n (smallest-divisor n)))

(define (smallest-divisor n)
	(find-divisor n 2))

(define (find-divisor n test-divisor)
	(cond ((> (square test-divisor) n) n)
		  ((divides? test-divisor n) test-divisor)
		  (else (find-divisor n (+ test-divisor 1)))))

(define (square n)
	(* n n))

(define (divides? a b)
	(= (remainder b a) 0))

;;; (prime? 1)
;;; (prime? 2)
;;; (prime? 3)
;;; (prime? 4)
;;; (prime? 5)
;;; (prime? 6)
;;; (prime? 7)
;;; (prime? 8)
;;; (prime? 9)
;;; (prime? 10)