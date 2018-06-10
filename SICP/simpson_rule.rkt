#lang racket

(define (cube x) (* x x x))

(define (sum term a next b)
  (if (> a b)
      0
      (+ (term a) 
         (sum term (next a) next b))))

(define (inc x) (+ x 1))

(define (simpson f a b n)
  (define h (/ (- b a) n))
  (define (yk k) (f (+ a (* k h))))
  (define (simpson-term k)
    (* (cond ((or (= k 0) (= k n)) 1)
             ((even? k) 4)
             (else 2))
       (yk k)))
  (* (/ h 3) (sum simpson-term 0 inc n)))

(simpson cube 0 1 100)
(simpson cube 0 1 1000)
(simpson cube 0 1 10000)
(simpson cube 0 1 100000)