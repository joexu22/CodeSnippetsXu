#lang racket
(require rackunit)

; golfed solution I found on internet
; this takes the ?define? for granted
(define (make-monitored f)
	(define times-called 0)
	(define (mf message)
		(cond ((eq? message 'how-many-calls?) times-called)
			((eq? message 'reset-count) (set! times-called 0))
			(else (set! times-called (+ times-called 1))
				(f message))))
	mf)

; this is my solution more in line with what is being taught
; implements my own counter procedure
(define (my-monitor f)

	(define (called-counter i)
		(define (return-counter m) i)
		(define (increment-counter m) (set! i (+ i 1)))
		(define (reset-counter m) (set! i 0))
		(define (counter n)
		(cond ((eq? n 'return-count) return-counter)
				((eq? n 'reset-count) reset-counter)
				((eq? n 'increment-count) increment-counter)))
		counter)
  
	(define count (called-counter 0))
	
	(define (mf message)
		(cond ((eq? message 'how-many-calls?) ((count 'return-count) 0))
			((eq? message 'reset-count) ((count 'reset-count) 0))
			(else ((count 'increment-count) 0)
					(f message))))
	mf)

(define s (make-monitored sqrt))
(s 100)
(s 'how-many-calls?)
(s 225)
(s 'how-many-calls?)
(s 'reset-count)
(s 'how-many-calls?)
(newline)
(define s2 (my-monitor sqrt))
(s2 100)
(s2 'how-many-calls?)
(s2 225)
(s2 'how-many-calls?)
(s2 'reset-count)
(s2 'how-many-calls?)