#lang racket
(sqrt 100)
(identity 100)

(define (make-accumulator acc)
  (lambda (x) (set! acc (+ acc x)) 
              acc))

(define A (make-accumulator 0))
(A 1)
(A 1)
