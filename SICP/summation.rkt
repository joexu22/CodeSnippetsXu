#lang racket

; Helper Functions
(define (cube n) (* n n n))
(define (inc n) (+ n 1))
(define (identity n) n)

; Code For Understanding Summation
(define (sum term a next b)
  (if (> a b)
    0
    (+ (term a)
       (sum term (next a) next b))))

(define (cube-sum a b)
  (sum cube a inc b))

(define (int-sum a b)
  (sum identity a inc b))

(define (pi-sum a b)
  (define (pi-term x) (/ 1.0 (* x (+ x 2))))
  (define (pi-next x) (+ x 4))
  (sum pi-term a pi-next b))

(cube-sum 1 10)
(int-sum 1 10)
(* 8 (pi-sum 1 10000))
