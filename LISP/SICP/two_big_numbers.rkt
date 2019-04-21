#lang racket

(define (square-sum-larger a b c)
  (define (<= x y) (or (< x y) (= x y)))
  (define (square x) (* x x))
  (define (sum_square x y) (+ (square x) (square y)))
  (cond 
    ((and (<= a b) (<= a c)) (sum_square b c))
    ((and (<= b a) (<= b c)) (sum_square a c))
    ((and (<= c a) (<= c b)) (sum_square a b))))

(square-sum-larger 1 2 3) ;expect 13
(square-sum-larger 1 3 2) ;expect 13
(square-sum-larger 2 1 3) ;expect 13
(square-sum-larger 2 3 1) ;expect 13
(square-sum-larger 3 1 2) ;expect 13
(square-sum-larger 3 2 1) ;expect 13

(square-sum-larger 10 10 3) ;expect 200
(square-sum-larger 15 10 5) ;expect 325
(square-sum-larger 7 8 9) ;expect 145
(square-sum-larger 12 8 12) ;expect 288
(square-sum-larger 7 2 3) ;expect 58
(square-sum-larger 4 4 4) ;expect 32
(square-sum-larger 1 1 1) ;expect 2