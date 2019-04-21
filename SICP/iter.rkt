#lang racket

(define (identity x) x)
(define (add-one x) (+ x 1))

(define (sum term a next b)
  (define (iter a result)
    (if (> a b)
      result
      (iter (next a) (+ result (term a)))))
  (iter a 0))

(sum identity 0 add-one 10)
(sum identity 0 add-one 8)
