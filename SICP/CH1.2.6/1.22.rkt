#lang racket
(require rackunit)

(define (prime? n)
	(= n (smallest-divisor n)))

(define (smallest-divisor n)
	(find-divisor n 2))

(define (find-divisor n test-divisor)
	(cond
		((> (square test-divisor) n) n)
		((divides? test-divisor n) test-divisor)
		(else (find-divisor n (+ test-divisor 1)))))

(define (square n)
	(* n n))

(define (divides? a b)
	(= (remainder b a) 0))

(define (timed-prime-test n)
	;;; (newline)
	;;; (display n)
	(start-prime-test n (current-inexact-milliseconds)))

(define (start-prime-test n start-time)
	(cond 
		((prime? n)
			(newline)
			(display n)
			(report-prime (- (current-inexact-milliseconds) start-time)))))

(define (report-prime elapsed-time)
	(display " *** ")
	(display elapsed-time))

(define (search-for-primes lower upper)
	(cond 
		((even? lower) (search-for-primes (+ lower 1) upper))
		((<= lower upper)
			(timed-prime-test lower)
			(search-for-primes (+ lower 2) upper))))

 (search-for-primes 1000 1019)       ; 1e3 
 (search-for-primes 10000 10037)     ; 1e4 
 (search-for-primes 100000 100043)   ; 1e5 
 (search-for-primes 1000000 1000037) ; 1e6 
 (newline) 
 (search-for-primes 1000000000 1000000021)       ; 1e9 
 (search-for-primes 10000000000 10000000061)     ; 1e10 
 (search-for-primes 100000000000 100000000057)   ; 1e11 
 (search-for-primes 1000000000000 1000000000063) ; 1e12 