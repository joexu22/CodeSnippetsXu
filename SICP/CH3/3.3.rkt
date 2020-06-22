#lang racket

(define (make-account balance password)
  (define (withdraw amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance)
        "Insufficient funds"))
  (define (deposit amount)
    (set! balance (+ balance amount))
    balance)
  (define (dispatch p m)
    (cond ((not (eq? p password)) (error "Incorrect password\n"))
          ((eq? m 'withdraw) withdraw)
          ((eq? m 'deposit) deposit)
          (else (error "Unknown request -- MAKE-ACCOUNT" m))))
  dispatch)

(define acc (make-account 100 'secret-password))
((acc 'secret-password 'withdraw) 40)
((acc 'secret-password 'withdraw) 40)
((acc 'secret-password 'deposit) 60)

;(define acc2 (make-account 100 'secret-password))
;((acc2 'secret-password 'fail) 40)

;(define acc3 (make-account 100 'secret-password))
;((acc3 'some-other-password 'deposit) 50)

;(define acc4 (make-account 100 'secret-password))
;((acc4 'some-other-password 'fail) 50)