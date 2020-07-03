#lang racket
(require rackunit)

; golfed solution I found on internet
; this takes the ?define? for granted
(define (make-monitored f)
	(define counter 0)
	(define (mf message)
		(cond
			((eq? message 'how-many-calls?) counter)
			((eq? message 'reset-count) (set! counter 0))
			(else (set! counter (+ counter 1))
				(f message))))
	mf)

; this is my solution more in line with what is being taught
; implements my own counter procedure
(define (called-counter i)
	(define (increment-counter m) (set! i (+ i 1)))
	(define (reset-counter m) (set! i 0))
	(define (return-counter m) i)
	(define (counter n)
		(cond
			((eq? n 'increment-count) increment-counter)
			((eq? n 'reset-count) reset-counter)
			((eq? n 'return-count) return-counter)))
	counter)

(define (my-monitor function)
	(define custom-counter (called-counter 0))
	(define (monitored-function message)
		(cond
			((eq? message 'how-many-calls?) ((custom-counter 'return-count) 0))
			((eq? message 'reset-count) ((custom-counter 'reset-count) 0))
			(else ((custom-counter 'increment-count) 0)
				(function message))))
	monitored-function)

;;; testing working solution from internet
(test-begin
	(let ([s (make-monitored sqrt)])
		(check-equal? (s 100) 10 "squareroot of 100 should be 10")
		(check-equal? (s 'how-many-calls?) 1 "Function should have been called 1 time")
		(check-equal? (s 225) 15 "squareroot of 225 shoudl be 15")
		(check-equal? (s 'how-many-calls?) 2 "Function should have been called 2 times")
		(s 'reset-count)
		(check-equal? (s 'how-many-calls?) 0 "Function should have been called 0 times after reset")))

;;; testing my called-counter function
(test-begin
	(let ([counter (called-counter 0)])
		(check = ((counter 'return-count) 0) 0)
		((counter 'increment-count) 0)
		(check = ((counter 'return-count) 0) 1)
		((counter 'increment-count) 1)
		(check = ((counter 'return-count) 0) 2)
		((counter 'reset-count) 0)
		(check = ((counter 'return-count) 0) 0)))

(test-begin
	(let ([s (my-monitor sqrt)])
		(check-equal? (s 100) 10 "squareroot of 100 should be 10")
		(check-equal? (s 'how-many-calls?) 1 "Function should have been called 1 time")
		(check-equal? (s 225) 15 "squareroot of 225 shoudl be 15")
		(check-equal? (s 'how-many-calls?) 2 "Function should have been called 2 times")
		(s 'reset-count)
		(check-equal? (s 'how-many-calls?) 0 "Function should have been called 0 times after reset")))
